#!/usr/bin/env python3
"""More involved type annotations"""

from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """It retrieve a value from a dictionary"""
    if key in dct:
        return dct[key]
    else:
        return default
