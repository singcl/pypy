# -*- coding: utf-8 -*-

"""
文件描述项目及其从属的文件

@Author Singcl<https://github.com/singcl>
@Version 0.0.1
@Data 2020/04/12
"""

from setuptools import find_packages, setup

setup(
    name='flaskr',
    version='1.0.0',
    packages= find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask'
    ]
)
