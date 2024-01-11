#!/usr/bin/env python3
"""Module for complex types - functions"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """It creates a multiplier function"""
    return lambda x: x * multiplier
