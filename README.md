**setuptools-golang-cli**

Расширение для setuptools собирающие CLI написанные на golang.

**Использование**

Добавьте setuptools-golang-cli в setup_requires вашего setup.py и 
build_golang_cli={'root': ...}. root ссылается на корень вашего go проекта.

В списке файлов с исходным кодом, который передается как аргумент при создании
экземпляра класса Extension может быть указан только один файл пакетом `main`.
Этот файл может импортировать другие пакеты.

```python
setup(
    ...
    build_golang_cli={'root': 'github.com/user/project'},
    ext_modules=[Extension('example', ['example.go'])],
    setup_requires=['setuptools-golang-cli'],
    ...
)
```