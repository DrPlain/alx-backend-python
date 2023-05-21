#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from client import GithubOrgClient
import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """ Class to test Github client """

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    def test_org(self, input):
        """ Test that GithubOrgClient returns correct value"""
        with patch('client.get_json') as mock_get_json:
            mock_get_json.assert_called_once_with(
                f'https://api.github.com/orgs/{input}')
