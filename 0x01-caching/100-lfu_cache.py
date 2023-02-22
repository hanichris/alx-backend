#!/usr/bin/env python3
"""Implementation of the LFU cache.

Count how often an item is needed. Those that are
used least often are discarded first. Similar in a
way to LRU.
"""
from typing import Optional, Union


BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """Implements the LFU cache."""

    def __init__(self) -> None:
        super().__init__()

        self.freq = {}

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
            least = min(self.freq.values())
            _key = list(filter(lambda x: self.age[x] == least, self.age))[0]
            print(f"DISCARD: {_key}")
            self.cache_data.pop(_key, None)
            self.age.pop(_key, None)

        self.cache_data[key] = item
        self.freq[key] = self.freq.get(key, 0) + 1


    def get(self, key: Optional[str]) -> Union[str, None]:
        """Return the value stored at the given key index.

        Args:
            key: index of interest.
        Return:
            str: value stored at the given key.
        """
        if key is not None and key in self.age.keys():
            self.freq[key] = self.freq.get(key, 0) + 1
            return self.cache_data.get(key)
        return None
