#!/usr/bin/env python3
"""Module containing `index_range` function definition."""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return the range of indexes for given pagination parameters.

    Args:
        page (int): page number which is 1-indexed, i.e, first page is page 1
        page_size (int): range of indexes that are of interest.
    Return:
        tuple[int, int]: start index and end index
    """
    return page_size * (page - 1), page_size * page
