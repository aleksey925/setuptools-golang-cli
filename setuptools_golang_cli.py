import contextlib
import copy
import os
import pipes
import shutil
import stat
import subprocess
import sys
import tempfile

from setuptools.command.build_ext import build_ext as _build_ext


@contextlib.contextmanager
def _tmpdir():
    tempdir = tempfile.mkdtemp()
    try:
        yield tempdir
    finally:
        def err(action, name, exc):
            # Windows не может удалить readonly файлы, делам их writeable
            os.chmod(name, stat.S_IWRITE)
            action(name)

        shutil.rmtree(tempdir, onerror=err)


def _check_call(cmd, cwd, env):
    envparts = [
        '{}={}'.format(k, pipes.quote(v))
        for k, v in sorted(tuple(env.items()))
    ]
    print(
        '$ {}'.format(' '.join(envparts + [pipes.quote(p) for p in cmd])),
        file=sys.stderr,
    )
    subprocess.check_call(cmd, cwd=cwd, env=dict(os.environ, **env))


def _get_build_extension_method(base, root):

    def build_extension(self, ext):
        def _raise_error(msg):
            raise IOError(
                'Error building extension `{}`: '.format(ext.name) + msg,
            )

        def build_in_temp_env():
            # Копирует пакет внутрь временного GOPATH окружения
            with _tmpdir() as tempdir:
                root_path = os.path.join(tempdir, 'src', root)
                os.makedirs(os.path.dirname(root_path))
                shutil.copytree('.', root_path)
                pkg_path = os.path.join(root_path, main_dir)

                env = {'GOPATH': tempdir}
                cmd_get = ('go', 'get', '-d')
                _check_call(cmd_get, cwd=pkg_path, env=env)

                cmd_build = (
                    'go', 'build', '-o',
                    os.path.abspath(self.get_ext_fullpath(ext.name)),
                    os.path.abspath(ext.sources[0])
                )
                _check_call(cmd_build, cwd=pkg_path, env=env)

        def build_in_user_env():
            pkg_path = os.path.split(os.path.abspath(ext.sources[0]))[0]

            cmd_get = ('go', 'get', '-d')
            _check_call(
                cmd_get, cwd=pkg_path, env={}
            )

            cmd_build = (
                'go', 'build', '-o',
                os.path.abspath(self.get_ext_fullpath(ext.name)),
                os.path.abspath(ext.sources[0])
            )
            _check_call(cmd_build, cwd=pkg_path, env={})

        if len(ext.sources) != 1:
            _raise_error(
                'sources must be a single file in the `main` package.\n'
                'Recieved: {!r}'.format(ext.sources)
            )

        # Если отсутствуют .go файлы, то родитель должен обработать это
        if not any(source.endswith('.go') for source in ext.sources):
            compiler = copy.deepcopy(self.compiler)
            self.compiler, compiler = compiler, self.compiler
            try:
                return base.build_extension(self, ext)
            finally:
                self.compiler, compiler = compiler, self.compiler

        main_file, = ext.sources
        if not os.path.exists(main_file):
            _raise_error('{} does not exist'.format(main_file))
        main_dir = os.path.dirname(main_file)

        if os.path.exists(os.environ.get('GOPATH', '')):
            build_in_user_env()
        else:
            build_in_temp_env()

    return build_extension


def _get_build_ext_cls(base, root):
    class build_ext(base):
        build_extension = _get_build_extension_method(base, root)

    return build_ext


def set_build_ext(dist, attr, value):
    root = value['root']
    base = dist.cmdclass.get('build_ext', _build_ext)
    dist.cmdclass['build_ext'] = _get_build_ext_cls(base, root)
