import click

from .commands import init as cmd_init


@click.group(context_settings={'help_option_names': ['-h', '--help']})
def main():
    """Snak helps you manage your dependencies """
    pass


@main.command()
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
