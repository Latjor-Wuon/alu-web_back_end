#!/usr/bin/env python3
"""
Module that provides string concatenation operations with type annotations.

This module contains functions for performing string operations
using Python 3 type annotations for better code clarity and type checking.
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenate two strings and return the result.

    Args:
        str1 (str): The first string to concatenate.
        str2 (str): The second string to concatenate.

    Returns:
        str: The concatenated string of str1 and str2.
    """
    return str1 + str2
