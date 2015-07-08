import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='aboardly',
    version='0.1.0',
    description='Official Aboardly API library client for python',
    author='Serge',
    author_email='info@aboardly.com',
    url='http://www.aboardly.com',
    license='MIT',
    url="https://github.com/herkyl/aboardly-python",
    download_url="https://github.com/herkyl/aboardly-python/archive/master.zip",
    install_requires=[
        'requests >= 2.1.0'
    ],
    packages=[
        'aboardly'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
