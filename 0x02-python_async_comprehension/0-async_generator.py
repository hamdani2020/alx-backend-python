#!/usr/bin/env python3
"""Module for task 0"""

import random
from typing import Generator
import asyncio


async def async_generator() -> Generator[float, None, None]:
    """The corountine will loop 10 times"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
