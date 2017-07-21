import json
import os

from .utils import Singleton


class Config(object):

    def __init__(self, filename='snak', prefix=''):
        self.conf = {}
        self.filename = filename
        self.prefix = prefix

    def get_filename(self, new_filename=None):
        filename = new_filename if new_filename else self.filename
        return os.path.join(self.prefix, filename + '.json')

    def load(self):
        with open(self.get_filename(), 'r') as conf_file:
            self.conf = json.loads(conf_file.read())
        return self

    def exists(self):
        return os.path.isfile(self.get_filename())

    def write(self, new_filename=None):
        with open(self.get_filename(new_filename), 'w') as conf_file:
            conf_file.write(str(self))

    def set(self, key, value):
        self.conf[key] = value
        return self

    def get(self, key, default=None):
        return self.conf.get(key, default)

    def __str__(self):
        return json.dumps(self.conf, indent=4, sort_keys=True)


class GlobalConfig(Config, metaclass=Singleton):
    """
    Same as Config but globally available
    """
    pass
