import os

import click

from .commands import init as cmd_init

_, current_folder = os.path.split(os.getcwd())


@click.group(context_settings={'help_option_names': ['-h', '--help']})
def main():
    """Snak helps you manage your dependencies """
    pass


@main.command()
@click.option('--name', prompt='Name',
                default=current_folder, help='Name of the project')
@click.option('--version', prompt='Version',
                default='1.0.0', help='Version of the project')
@click.option('--author', prompt='Author',
                default='', help='Name of the author')
@click.option('--description', prompt='Description',
                default='', help='Description of the project')
def init(*args, **kwargs):
    """
    Create a new python project
    """
    cmd_init(*args, **kwargs)


@main.command()
def install():
    """
    Install
    """
    pass
