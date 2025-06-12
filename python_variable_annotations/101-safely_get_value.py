#!/usr/bin/env python3
"""
Module that provides safe dictionary operations with generic type annotations.

This module contains functions for safely accessing dictionary values
using Python 3 generic types with TypeVar and Mapping.
"""

from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely get a value from a mapping with a default fallback.

    Args:
        dct (Mapping): A mapping (dictionary-like) object.
        key (Any): The key to look up in the mapping.
        default (Union[T, None]): The default value to return if key is not found.

    Returns:
        Union[Any, T]: The value from the mapping if key exists,
                      otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
