import unittest

import dict_utils


class TestRemoveNoneValueFromDict(unittest.TestCase):
    def test_remove_none_value_level_1(self):
        expected = {
            'key2': 'value2'
        }
        actual = {
            'key1': None,
            'key2': 'value2'
        }
        self.assertDictEqual(expected, dict_utils.remove_none_values(actual))

    def test_remove_none_value_level_2(self):
        expected = {
            'key1': {
                'key11': 'value11'
            }
        }
        actual = {
            'key1': {
                'key11': 'value11',
                'key12': None,
            }
        }
        self.assertDictEqual(expected, dict_utils.remove_none_values(actual))

    def test_remove_none_value_level_3(self):
        expected = {
            'key1': {
                'key11': {
                    'key111': 'value111',
                },
            }
        }
        actual = {
            'key1': {
                'key11': {
                    'key111': 'value111',
                    'key112': None,
                },
                'key22': {
                    'key31': None,
                }
            }
        }
        self.assertDictEqual(expected, dict_utils.remove_none_values(actual))


if __name__ == '__main__':
    unittest.main()
