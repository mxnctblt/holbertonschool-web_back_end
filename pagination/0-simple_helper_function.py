#!/usr/bin/env python3
"""
task 0. Simple helper function
"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ return a tuple containing a start index and an end index """
    return ((page_size * (page - 1)), page_size * page)
