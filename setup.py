#!/usr/bin/env python

import chosen

try:
	from setuptools import setup, find_packages
except ImportError:
	from ez_setup import use_setuptools
	use_setuptools()
	from setuptools import setup, find_packages

setup(
    name='django-chosen-mega',
    version=chosen.__version__,
    description='django FormFields using the Chosen javascript plugin for jQuery',
    author='Chris Spencer',
    author_email='chrisspen@gmail.com',
    url='https://github.com/chrisspen/django-chosen',
    packages=find_packages(),
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
	install_requires=[
		'Django>=1.4',
	],
	include_package_data=True,
	zip_safe=False,
)

