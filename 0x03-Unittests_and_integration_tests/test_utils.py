#!/usr/bin/env python3
"""
Module for testing utils module
"""

import unittest
from typing import Tuple, Union, Dict
from parameterized import parameterized
from unittest.mock import patch, Mock

from utils import access_nested_map, get_json, memorize


class TestAccessNestedMap(unittest.TestCase):
    """This class test the access_nested_map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int],
            ) -> None:
        """
        This is a test access_nested_map output
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expception: Exception,
            ) -> None:
        """ A test for access_nested_map exception raising output"""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)
