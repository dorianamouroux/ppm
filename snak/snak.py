import click

from .commands import Init


@click.group(context_settings={'help_option_names': ['-h', '--help']})
def main():
    """Snak helps you manage your dependencies """
    pass


@main.command()
def init(*args, **kwargs):
    """
    Create a new python project
    """
    cmd = Init(*args, **kwargs)
    cmd.run()


@main.command()
def install():
    """
    Install
    """
    pass
