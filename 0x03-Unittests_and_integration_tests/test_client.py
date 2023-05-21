#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """ Class to test Github client """

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, input, mock_get_json):
        """ Test that GithubOrgClient returns correct value"""
        obj = GithubOrgClient(input)
        obj.org()
        mock_get_json.assert_called_once_with(
                f'https://api.github.com/orgs/{input}')
