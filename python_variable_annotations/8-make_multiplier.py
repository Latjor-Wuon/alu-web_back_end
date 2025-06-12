#!/usr/bin/env python3
"""
Module that provides higher-order functions with complex type annotations.

This module contains functions that return other functions
using Python 3 type annotations including Callable types.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a float by a given multiplier.

    Args:
        multiplier (float): The multiplier value to be used by the returned function.

    Returns:
        Callable[[float], float]: A function that takes a float and returns
                                 the product of that float and the multiplier.
    """
    def multiply(value: float) -> float:
        """
        Multiply the input value by the multiplier.

        Args:
            value (float): The value to multiply.

        Returns:
            float: The product of value and multiplier.
        """
        return value * multiplier
    
    return multiply
