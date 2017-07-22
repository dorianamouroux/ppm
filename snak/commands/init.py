import os
from collections import namedtuple

import click

from ..config import GlobalConfig


_, current_folder = os.path.split(os.getcwd())
UserInput = namedtuple('UserInput', ['name', 'version', 'author', 'description'])


class Init(object):

    def __init__(self, filename=None):
        self.config = GlobalConfig(filename)
        self.default = UserInput(current_folder, '1.0.0', '', '')
        if self.config.exists():
            self.import_default_from_existing_config()

    def import_default_from_existing_config(self):
        click.echo('{} found ! Using it for default values.'\
            .format(self.config.get_filename()))
        self.config.load()
        self.default = UserInput(self.config.get('name'),
                        self.config.get('version'),
                        self.config.get('author'),
                        self.config.get('description'))

    def run(self):
        user_input = self.prompt_information()
        conf = self.build_conf(user_input)
        click.echo(conf)
        click.confirm('Is that correct ?', default=True, abort=True)
        conf.write()
        click.echo(conf.get_filename() + ' written !')

    def prompt_information(self):
        return UserInput(
            click.prompt('Name', default=self.default.name),
            click.prompt('Version', default=self.default.version),
            click.prompt('Author', default=self.default.author),
            click.prompt('Description', default=self.default.description))

    def build_conf(self, user_input):
        return self.config\
                .set('name', user_input.name)\
                .set('version', user_input.version)\
                .set('author', user_input.author)\
                .set('description', user_input.description)
