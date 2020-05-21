#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='acgv1signer',
    version=1.1,
    description=(
        'BaiduCloud-V1-auth'
    ),
    long_description=open('README.rst').read(),
    author='galvinwang',
    author_email='137606834@qq.com',
    maintainer='galvinwang',
    maintainer_email='137606834@qq.com',
    license='BSD License',
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/Galvin-wjw/ACG-Samples/blob/master/acgv1signer/acgv1signer.py',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries'
    ]
)