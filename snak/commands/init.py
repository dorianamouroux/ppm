import click


def init(name, version, author, description):
    click.echo('init')
    click.echo(name)
    click.echo(version)
    click.echo(author)
    click.echo(description)
