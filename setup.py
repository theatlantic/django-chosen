#!/usr/bin/env python

import os

from setuptools import setup, find_packages

import chosen

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))

def get_reqs(*fns):
    lst = []
    for fn in fns:
        for package in open(os.path.join(CURRENT_DIR, fn)).readlines():
            package = package.strip()
            if not package:
                continue
            lst.append(package.strip())
    return lst

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
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.6",
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=get_reqs('requirements-min-django.txt', 'requirements.txt'),
    tests_require=get_reqs('requirements-test.txt'),
)
