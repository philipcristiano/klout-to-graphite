#!/usr/bin/env python
import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def run_setup():
    setup(
        name='klout-to-graphite',
        version='0.0.3',
        description='A tool to send Klout scores to Graphite',
        keywords = 'klout graphite',
        url='https://github.com/philipcristiano/klout-to-graphite',
        author='Philip Cristiano',
        author_email='philipcristiano@gmail.com',
        license='BSD',
        packages=['klout_to_graphite'],
        install_requires=[
            'Klout==0.1.0',
        ],
        test_suite='tests',
        long_description=read('README.md'),
        zip_safe=True,
        classifiers=[
        ],
        entry_points="""
        [console_scripts]
        klout-to-graphite=klout_to_graphite:main
        """,
    )

if __name__ == '__main__':
    run_setup()
