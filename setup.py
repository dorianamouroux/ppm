from setuptools import setup, find_packages

from snak.__version__ import version

setup(name='snak',
    version=version,
    description='The packet manager for modern Python world',
    url='http://github.com/dorianamouroux/snak',
    author='Dorian Amouroux',
    author_email='dor.amouroux@gmail.com',
    license='MIT',
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        'click',
    ],
    entry_points = {
        'console_scripts': [
            'snak=snak.snak:main'
        ],
    },
    test_suite='nose.collector',
    tests_require=['nose'],
)
