#!/usr/bin/env python

from setuptools import setup, find_packages


desc = """



setup(
    name='urlfh',
    version='0.0.2',
    author='Terrence Meiczinger',
    author_email='terrence72@gmail.com',
    license='LICENSE',
    url='https://github.com/tmeiczin/urlfh',
    download_url='https://github.com/tmeiczin/urlfh',
    description='URL file handle',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=False,
    python_requires=">=2.7",
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Utilities',
    ],
    install_requires=[
        'requests',
    ],
)
