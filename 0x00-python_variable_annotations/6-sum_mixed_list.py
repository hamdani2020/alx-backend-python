#!/usr/bin/env python3
"""Modules for complex types - mixed list"""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """It takes a list mxd_list of integers and floats
    and return their sum as float
    """
    return float(sum(mxd_list))
