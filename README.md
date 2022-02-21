# douyin_image [![Version][version-badge]][version-link] ![MIT License][license-badge]


test python project upload github and trigger update pypi


`print_text` Is a personal test that prints strings


### Examples


### use

```
from print_text import add,remove,update
print(add.make())
print(remove.make())
print(update.make())
```


### install

```
$ pip install print_text
```


### License

[MIT](https://github.com/pythonml/douyin_image/blob/master/LICENSE)


[version-badge]:   https://img.shields.io/badge/version-0.1-brightgreen.svg
[version-link]:    https://pypi.python.org/pypi/douyin_image/
[license-badge]:   https://img.shields.io/github/license/pythonml/douyin_image.svg

### Method of building library
1. cd test_github_release_pypi
```
python setup.py sdist bdist_wheel
```

2. The above command will generate a tar in the ```dist/``` directory GZ source package and one Wheel package for wheel.
```
dist/
  print_text-0.1-py3-none-any.whl
  print_text-0.1.tar.gz
```

3. We can verify whether our project can be successfully installed from the local installation library, as follows
```
pip install dist/print_text-0.1-py3-none-any.whl
```

4. Upload the project to pypi. We use ```twin``` to upload the project. First install ```twin```.
```
# install
pip install twine
# upload
twine upload dist/*
```
#### Method of building library(github)
1. test_github_release_pypi(Github) -> Settings -> Secrets: Used to manage users and passwords of PyPi
2. test_github_release_pypi(Github) -> Actions -> .github/workflows: Used to create trigger workflows 
