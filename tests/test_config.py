import os
import json
from unittest import TestCase

from snak.config import Config

from .utils import generate_token, force_rm, ordered, compare_json_file


class ConfigTest(TestCase):

    def setUp(self):
        self.base_dir = os.path.dirname(os.path.realpath(__file__))
        self.assets_dir = os.path.join(self.base_dir, 'assets')
        self.random_conf_name = generate_token()
        self.random_conf_name_2 = generate_token()

    def test_filename(self):
        conf = Config('test', '../..')
        self.assertEqual(conf.get_filename(), '../../test.json')
        conf = Config('test')
        self.assertEqual(conf.get_filename(), 'test.json')
        conf = Config()
        self.assertEqual(conf.get_filename(), 'snak.json')

    def test_load(self):
        conf = Config('conf', self.assets_dir)
        conf.load()
        self.assertEqual(conf.get('name'), 'test')

    def test_write(self):
        conf = Config(self.random_conf_name, self.assets_dir)
        conf.set('test', '4')
        conf.write()
        with open(conf.get_filename()) as conf_on_disk:
            result = json.loads(conf_on_disk.read())
            self.assertEqual(ordered({"test": "4"}), ordered(result))

    def test_load_and_write_exact(self):
        conf = Config('conf', self.assets_dir).load()
        conf.write(self.random_conf_name_2)
        f1 = conf.get_filename()
        f2 = conf.get_filename(self.random_conf_name_2)
        self.assertTrue(compare_json_file(f1, f2))

    def tearDown(self):
        """
        Remove file created in test_save and test_load_and_write_exact
        """
        name = os.path.join(self.assets_dir, self.random_conf_name + '.json')
        force_rm(name)
        name = os.path.join(self.assets_dir, self.random_conf_name_2 + '.json')
        force_rm(name)
