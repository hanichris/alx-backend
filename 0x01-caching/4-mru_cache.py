#!/usr/bin/env python3
"""Implementation of the MRU cache.

Discard the most recently used items first. Made possible
by keeping track of what was used when through 'age-bits'.
"""
from typing import Optional, Union


BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """Implements the MRU cache."""

    def __init__(self) -> None:
        super().__init__()

        self.age = {}
        self.count = 0

    def put(self, key: Optional[str], item: Optional[str]) -> None:
        """Add an item to the cache.

        If the number of elements in the cache exceeds the set
        `MAX_ITEMS`, first discard the most recently used element
        in the cache.
        Args:
            key: index of the item to be added.
            item: the value to be added at the given index.
        """
        if key is None or item is None:
            return

        if key not in self.cache_data and\
           len(self.cache_data) >= self.MAX_ITEMS:
            max = max(self.age.values())
            _key = list(filter(lambda x: self.age[x] == max, self.age))[0]
            print(f"DISCARD: {_key}")
            self.cache_data.pop(_key, None)
            self.age.pop(_key, None)

        self.cache_data[key] = item
        self.age[key] = self.count
        self.count += 1

    def get(self, key: Optional[str]) -> Union[str, None]:
        """Return the value stored at the given key index.

        Args:
            key: index of interest.
        Return:
            str: value stored at the given key.
        """
        if key is not None and key in self.age.keys():
            self.age[key] = self.count
            self.count += 1
            return self.cache_data.get(key)
        return None
