import io

from setuptools.command import easy_install
from contextlib import redirect_stdout


def install(package_name):
    with io.StringIO() as buf, redirect_stdout(buf):
        easy_install.main([package_name])
        output = buf.getvalue()
    print('----------')
    print(output)
