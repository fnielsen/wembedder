"""For packaging and installation."""

import os

from setuptools import setup

import versioneer


filename = os.path.join(os.path.dirname(__file__), 'requirements.txt')
requirements = open(filename).read().splitlines()


setup(
    name='wembedder',
    packages=['wembedder'],
    version='0.1',
    author='Finn Aarup Nielsen',
    author_email='faan@dtu.dk',
    description='Wikidata embedding',
    license='Apache License 2.0',
    keywords='embedding',
    url='https://github.com/fnielsen/wembedder',
    package_data={'wembedder': ['data/*.csv']},
    long_description='',
    classifiers=[
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        ],
    cmdclass==versioneer.get_cmdclass(),
    install_requires=requirements,
    version=versioneer.get_version(),
)
