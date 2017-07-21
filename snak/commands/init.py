import os

import click

from ..config import GlobalConfig


_, current_folder = os.path.split(os.getcwd())


def init():
    name = click.prompt('Name', default=current_folder)
    version = click.prompt('Version', default='1.0.0')
    author = click.prompt('Author', default='')
    description = click.prompt('Description', default='')
    conf = GlobalConfig()
    conf.set('name', name)
    conf.set('version', version)
    conf.set('author', author)
    conf.set('description', description)
    conf.set('dependencies', {})
    click.echo(conf)
    click.confirm('Is that correct ?', default=True, abort=True)
    conf.write()
    click.echo(conf.get_filename() + ' written !')
