#!/usr/bin/env python3
"""More involved type annotations"""

from typing import Mapping, Any, TypeVar, Union

DF = Union[TypeVar, None]
R = Union[Any, TypeVar]


def safely_get_value(dct: Mapping, key: Any, default: DF = None) -> R:
    """It retrieve a value from a dictionary"""
    if key in dct:
        return dct[key]
    else:
        return default
