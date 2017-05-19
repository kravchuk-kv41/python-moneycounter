import io
import unittest
import json
import yaml
import pickle
import counter


class StringTest(unittest.TestCase):

    test_data = [{"data": "16 May 2017", "description": "donate1", "money": 100},
                 {"data": "16 May 2017", "description": "donate2", "money": 100},
                 {"data": "16 May 2017", "description": "donate3", "money": 100},
                 {"data": "16 May 2017", "description": "donate4", "money": 100},
                 {"data": "16 May 2017", "description": "donate5", "money": 100}]

    def test_pickle_format(self):
        # test load
        counter.Counter().set_configuration("configuration.cfg", "serialization", "type", "pickle")
        self.assertEqual(self.test_data, counter.Counter().load_data(io.BytesIO(pickle.dumps(self.test_data))))

        # test save
        counter.Counter().set_configuration("configuration.cfg", "serialization", "type", "pickle")
        self.assertEqual(self.test_data, counter.Counter().save_data(io.BytesIO(), self.test_data))

    def test_json_format(self):
        # test load
        file = io.StringIO(json.dumps(self.test_data))
        counter.Counter().set_configuration("configuration.cfg", "serialization", "type", "json")
        self.assertEqual(self.test_data, counter.Counter().load_data(file))

        # test save
        counter.Counter().set_configuration("configuration.cfg", "serialization", "type", "json")
        self.assertEqual(self.test_data, counter.Counter().save_data(io.StringIO(), self.test_data))

    def test_yaml_format(self):
        # test load
        file = io.StringIO(yaml.dump(self.test_data))
        counter.Counter().set_configuration("configuration.cfg", "serialization", "type", "yaml")
        self.assertEqual(self.test_data, counter.Counter().load_data(file))

        # test save
        counter.Counter().set_configuration("configuration.cfg", "serialization", "type", "yaml")
        self.assertEqual(self.test_data, counter.Counter().save_data(io.StringIO(), self.test_data))