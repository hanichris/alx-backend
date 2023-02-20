#!/usr/bin/env python3
"""Module combines index_range implementation with a class definintion"""
import csv
import math
from typing import List


index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.

    Attributes:
        DATA_FILE (str): name of csv file representing database.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return a page through correct pagination of the dataset.

        Args:
            page (int): page number which is 1-indexed.
            page_size (int): number of elements to list on the page.
        Return:
            list[list]: content of the page.
        """
        assert type(page) is int
        assert type(page_size) is int
        assert page > 0
        assert page_size > 0
        start_index, end_index = index_range(page, page_size)

        return self.dataset()[start_index: end_index]
