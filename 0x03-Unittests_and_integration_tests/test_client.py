#!/usr/bin/env python3
"""
This a module for client test
"""

from typing import Dict
import unittest
from unittest.mock import(
    MagicMock,
    Mock,
    PropertyMock,
    patch,
)

from requests import HTTPError
from parameterized import parameterized, parameterized_class

from client import (
    GithubOrgClient
)
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """
    This is test for GithubOrgClient class
    """
    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch(
        "client.get_json",
    )
    def test_org(self, org: str, res: Dict, mocked_func: MagicMock) -> None:
        """
        Test for org method
        """
        mocked_func.return_value = MagicMock(return_value=res)
        Goc = GithubOrgClient(org)
        self.assertEqual(Goc.org(), res)
        mocked_func.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org)
        )
