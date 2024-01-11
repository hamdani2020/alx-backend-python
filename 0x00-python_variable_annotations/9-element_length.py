#!/usr/bin/env python3
"""Module iterable object"""

from typing import List, Sequence, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """It calculates the size of the elements in the sequence"""
    return [(i, len(i)) for i in lst]
