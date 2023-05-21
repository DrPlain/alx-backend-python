#!/usr/bin/env python3
import unittest
from unittest.mock import patch, PropertyMock
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

    def test_public_repos_url(self):
        """ Test that the named methid works as expected"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock:
            payload = {"repos_url": "Hello world"}
            mock.return_value = payload
            obj = GithubOrgClient("testing")
            result = obj._public_repos_url
            self.assertEqual(result, payload['repos_url'])

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, key, expected):
        """pass"""
        result = GithubOrgClient.has_license(repo, key)
        self.assertEqual(result, expected)
