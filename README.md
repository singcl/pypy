# Python

Python 之路

_The way to Python._

## virtualenv 安装 Py2 Py3

```sh
# Python27 虚拟环境
virtualenv -p C:/Python27/python.exe py2

# Python3x 虚拟环境
virtualenv -p C:/Python3x/python.exe py3

# activate in cmd
cd py3/Scripts/
activate

# activate in bash
source ./py3/Scripts/activate
```

## Vscode 中使用 virtualenv

https://segmentfault.com/q/1010000011089735

```sh
# PyCryptodome is a self-contained Python package of low-level cryptographic primitives.
# It supports Python 2.6 and 2.7, Python 3.4 and newer, and PyPy.
# All modules are installed under the Crypto package.
#You can install it with:
pip install pycryptodome

# 如果之前安装过crypto 模块的话先卸载crypto在手动删除site-packages 下的crypto文件 在安装pycryotodome
# 不然会安装失败
```

#生成requirements.txt
python项目中必须包含一个 requirements.txt 文件，用于记录所有依赖包及其精确的版本号。以便新环境部署。

```sh
# 自动生成
(venv) $ pip freeze > requirements.txt
# 安装
(venv) $ pip install -r requirements.txt
```

