from setuptools import setup
import setuptools
import os
import sys

_here = os.path.abspath(os.path.dirname(__file__))

if sys.version_info[0] < 3:
    with open(os.path.join(_here, 'README.rst')) as f:
        long_description = f.read()
else:
    with open(os.path.join(_here, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()

version = {}
with open(os.path.join(_here, 'threet.chatbot.tele', 'version.py')) as f:
    exec(f.read(), version)

setup(
    name='threet.chatbot.tele',
    version=version['__version__'],
    description=('Show how to structure a Python project.'),
    long_description=long_description,
    author='3T',
    author_email='trungthanh.tran@live.com',
    url='https://github.com/bast/somepackage',
    license='MPL-2.0',
    packages=setuptools.find_packages(),
    include_package_data=True,
    )