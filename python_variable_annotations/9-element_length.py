#!/usr/bin/env python3
"""
Module that provides iterable operations with duck typing annotations.

This module contains functions for processing iterables
using Python 3 duck typing with Iterable and Sequence types.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples containing each element and its length.

    Args:
        lst (Iterable[Sequence]): An iterable of sequences (strings, lists,
                                 etc.).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple contains
                                   a sequence from the input and its length.
    """
    return [(i, len(i)) for i in lst]
