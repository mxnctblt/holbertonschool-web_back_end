#!/usr/bin/env python3
""" task 8. Complex types - functions """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ type-annotated function make_multiplier """
    def n(num: float):
        return num * multiplier
    return n
