#!/usr/bin/env python3
""" task 6. Complex types - mixed list """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ type-annotated function sum_mixed_list """
    return sum(mxd_lst)
