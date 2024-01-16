#!/usr/bin/env python3
"""Module for task 1"""

from importlib import import_module as using
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """It generates a list of 10 numbers for a generator"""
    return [num async for num in async_generator()]
