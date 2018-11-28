# coding: UTF-8
from setuptools import find_packages
from setuptools import setup


def _load_requires_from_file(filepath):
    return [pkg_name.rstrip('\r\n') for pkg_name in open(filepath).readlines()
            if pkg_name in'=']


def _install_requires():
    return _load_requires_from_file('requirements.txt')


def _packages():
    return find_packages(
        exclude=[
            '*.tests',
            '*.tests.*',
            'tests.*',
            'tests'
        ]
    )


if __name__ == '__main__':
    setup(
        setup_requires=['pbr>=1.8'],
        pbr=True,
        version='0.0.1',
        author='yamamo-i',
        description='x-protocol-test',
        packages=_packages(),
        install_requires=_install_requires(),
    )
