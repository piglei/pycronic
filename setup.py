# -*- coding: utf-8 -*-
from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='pycronic',
    version='0.0.5',
    description='A crontab script wrapper written by python',
    long_description=readme(),
    author='piglei',
    url='https://github.com/piglei/pycronic/',
    keywords='crontab cronic',
    author_email='piglei2007@gmail.com',
    license='GPL',
    packages=['pycronic'],
    install_requires=[
        'configobj',
        'sender',
    ],
    classifiers=[
      "Programming Language :: Python :: 3",
      "Programming Language :: Python :: 2.7",
    ],
    scripts=['pycronic/cronic'],
    zip_safe=False)


