# douyin_image [![Version][version-badge]][version-link] ![MIT License][license-badge]


test python project upload github and trigger update pypi


`print_text` 是一个个人测试,打印字符串


### 示例


### 使用方式

```
from print_text import add,remove,update
print(add.make())
print(remove.make())
print(update.make())
```


### 安装

```
$ pip install print_text
```


### License

[MIT](https://github.com/pythonml/douyin_image/blob/master/LICENSE)


[version-badge]:   https://img.shields.io/badge/version-0.1-brightgreen.svg
[version-link]:    https://pypi.python.org/pypi/douyin_image/
[license-badge]:   https://img.shields.io/github/license/pythonml/douyin_image.svg

### 构建库的方法
1. cd test_github_release_pypi
```
python setup.py sdist bdist_wheel
```

2. 上面的命令会在dist/目录下生成一个tar.gz的源码包和一个.whl的Wheel包。
```
dist/
  print_text-0.1-py3-none-any.whl
  print_text-0.1.tar.gz
```

3. 打包完之后，我们可以从本地安装库，来验证我们的项目能否被成功安装，如下
```
pip install dist/print_text-0.1-py3-none-any.whl
```

4. 上传项目到PyPI，我们使用twine上传项目，先安装twine.
```
# install
pip install twine
# upload
twine upload dist/*
```