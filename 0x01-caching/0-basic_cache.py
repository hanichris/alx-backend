#!/usr/bin/env python3
"""Implementation of a caching system."""
from typing import Optional, Union


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Caching system."""

    def put(self, key: Optional[str], item: Optional[str]) -> None:
        """Add an item to the cache.

        Args:
            key: index of the item.
            item: value to store at given index.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key: Optional[str]) -> Union[str, None]:
        """Obtain the value stored at the given key.

        Args:
            key: index to query.
        """
        return self.cache_data.get(key)
