#!/usr/bin/env python3
"""
Module that provides basic arithmetic operations with type annotations.

This module contains functions for performing basic mathematical operations
using Python 3 type annotations for better code clarity and type checking.
"""


def add(a: float, b: float) -> float:
    """
    Add two floating point numbers and return their sum.

    Args:
        a (float): The first floating point number.
        b (float): The second floating point number.

    Returns:
        float: The sum of a and b.
    """
    return a + b
