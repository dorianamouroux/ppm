import click

from ..config import GlobalConfig


def init(name, version, author, description):
    click.echo('init')
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
