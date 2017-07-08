from setuptools import setup

setup(name='snak',
    version='0.1',
    description='The packet manager for modern Python world',
    url='http://github.com/dorianamouroux/snak',
    author='Dorian Amouroux',
    author_email='dor.amouroux@gmail.com',
    license='MIT',
    packages=['snak'],
    install_requires=[
        'click',
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
)
