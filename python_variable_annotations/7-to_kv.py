#!/usr/bin/env python3
"""
Module that provides tuple operations with complex type annotations.

This module contains functions for creating tuples with mixed types
using Python 3 type annotations including Tuple and Union types.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple with a string and the square of a number.

    Args:
        k (str): The string to be the first element of the tuple.
        v (Union[int, float]): The number to be squared for the second element.

    Returns:
        Tuple[str, float]: A tuple where the first element is the string k
                          and the second element is the square of v as a float.
    """
    return (k, float(v * v))
