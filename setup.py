try:
	from setuptools import setup, find_packages
	from os import path
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Python Utilities',
	'author': 'Brian Cullen',
	'author_email': 'brianshan@gmail.com',
	'version': '0.1',
	'install_requires': [],
	'packages': find_packages(exclude=['*.tests.*', '*.tests']),
	'name': 'myutils'
}

setup(**config)
