#!/usr/bin/env python3
""" Duck typing"""

from typing import Union, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """This function retrieve the first element in the list
    """
    if lst:
        return lst[0]
    else:
        return None
