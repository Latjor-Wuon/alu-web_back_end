#!/usr/bin/env python3
"""
Module that provides safe sequence operations with duck typing annotations.

This module contains functions for safely accessing sequence elements
using Python 3 duck typing with Sequence and Any types.
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Safely return the first element of a sequence or None if empty.

    Args:
        lst (Sequence[Any]): A sequence of any type of elements.

    Returns:
        Union[Any, None]: The first element of the sequence if it exists,
                         otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
