import click

from .commands import Init


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
def install():
    """
    Install
    """
    pass
