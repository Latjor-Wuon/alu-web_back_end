#!/usr/bin/env python3
"""
Module that provides array operations with proper type checking.

This module contains functions for array manipulation
that pass mypy type checking validation.
"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Create a zoomed array by repeating each element factor times.

    Args:
        lst (Tuple): A tuple of elements to zoom.
        factor (int): The number of times to repeat each element.

    Returns:
        List: A list with each element from lst repeated factor times.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
