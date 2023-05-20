#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """ Test class for testing access_nested_map"""

    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2)
    ])
    def test_access_nested_map(self, map, path, expected_res):
        """ Test that correct values are returned for a valid key"""
        with self.subTest(map=map, path=path, expected_res=expected_res):
            self.assertEqual(access_nested_map(map, path), expected_res)

    @parameterized.expand([
        ({}, ["a"]),
        ({"a": 1}, ["a", "b"]),
    ])
    def test_access_nested_map_exception(self, map, path):
        """ Test that keyErrors are raised for invalid key"""
        with self.assertRaises(KeyError):
            result = access_nested_map(map, path)


class TestGetJson(unittest.TestCase):
    """ Test class for get_json function """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """ Mock the requests.get method """
        mock_response = mock_get.return_value
        mock_response.json.return_value = test_payload
        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)
