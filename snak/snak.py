import click

from .commands import Init
from .commands.install import install as cmd_install


@click.group(context_settings={'help_option_names': ['-h', '--help']})
@click.option('--config', default='snak')
@click.pass_context
def main(ctx, config):
    """Snak helps you manage your pip dependencies """
    ctx.obj['CONFIG_FILE'] = config


@main.command()
@click.pass_context
def init(ctx):
    """
    Create a new python project
    """
    cmd = Init(ctx.obj.get('CONFIG_FILE'))
    cmd.run()


@main.command()
@click.argument('package_name', default='')
@click.pass_context
def install(ctx, package_name):
    """
    Install
    """
    cmd_install(package_name)
