#!/usr/bin/env python3
"""Implementation of the LIFO cache.

This cache behaves like the FIFO queue. Blocks are
evicted in the order that they were added without
regard to anything.
"""
from typing import Optional, Union


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Implements the FIFO cache."""

    def put(self, key: Optional[str], item: Optional[str]) -> None:
        """Add an item to the cache as in a LIFO queue.

        If the number of elements in the cache exceeds the set
        `MAX_ITEMS`, first discard the last element in the cache.
        Args:
            key: index of the item to be added.
            item: the value to be added at the given index.
        """
        if key not in self.cache_data and\
           len(self.cache_data) >= self.MAX_ITEMS:
            print(f"DISCARD: {self.cache_data.popitem()[0]}")

        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key: Optional[str]) -> Union[str, None]:
        """Return the value stored at the given key index.

        Args:
            key: index of interest.
        Return:
            str: value stored at the given key.
        """
        if key is None:
            return None
        return self.cache_data.get(key)
