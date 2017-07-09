from setuptools import setup

from snak.__version__ import version

setup(name='snak',
    version=version,
    description='The packet manager for modern Python world',
    url='http://github.com/dorianamouroux/snak',
    author='Dorian Amouroux',
    author_email='dor.amouroux@gmail.com',
    license='MIT',
    packages=['snak'],
    install_requires=[
        'click',
    ],
    scripts=['bin/snak'],
    test_suite='nose.collector',
    tests_require=['nose'],
)
