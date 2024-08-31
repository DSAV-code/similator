#Copyright 2024 Diego San Andrés Vasco

"""
This file is part of Similator.

Similator is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

Similator is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with Similator. If not, see <https://www.gnu.org/licenses/>.
"""

import json
from collections import OrderedDict
from typing import Any

class Memory:
    """A class to manage a cache for storing search results with a defined maximum size.
    
    Args:
        max_size (int): The maximum number of items the cache can hold.
    
    Attributes:
        max_size (int): The maximum size of the cache.
        memory (OrderedDict): The internal cache storage. Stores items in insertion order.
    
    Example:
        >>> memory = Memory(max_size=3)
        >>> memory.add_to_memory("key1", "value1")
        >>> memory.add_to_memory("key2", "value2")
        >>> memory.get_from_memory("key1")
        'value1'
        >>> memory.add_to_memory("key3", "value3")
        >>> memory.add_to_memory("key4", "value4")
        >>> memory.get_from_memory("key2")
        'value2'
        >>> memory.get_from_memory("key1")
        None  # Because "key1" was the oldest and removed when adding "key4"
        >>> memory.cls()
        >>> memory.memory
        OrderedDict()
        
    """
    
    def __init__(self, max_size: int = 100) -> None:
        if max_size <= 0:
            raise ValueError("max_size must be a positive integer.")
        self.max_size = max_size
        self.memory = OrderedDict()

    def add_to_memory(self, key: Any, value: Any) -> None:
        """Adds a key-value pair to the cache. If the cache exceeds the maximum size, the oldest item is removed.
        
        Args:
            key (Any): The key to be stored in the cache.
            value (Any): The value associated with the key.

        """
        if key in self.memory:
            # Remove the existing item before re-adding to maintain order
            del self.memory[key]
        elif len(self.memory) >= self.max_size:
            # Remove the oldest item
            self.memory.popitem(last=False)
        
        # Add the new item
        self.memory[key] = value

    def get_from_memory(self, key: Any) -> Any:
        """Retrieves a value from the cache based on the key.
        
        Args:
            key (Any): The key to search for in the cache.
        
        Returns:
            Any: The value associated with the key if found, else None.

        """
        return self.memory.get(key, None)

    def cls(self) -> None:
        """Clears the cache, removing all stored key-value pairs."""
        self.memory.clear()

    def load_memory(self, file_path: str) -> None:
        """Loads cache data from a JSON file into the memory. This overwrites any existing data in memory.
        
        Args:
            file_path (str): The path to the JSON file containing cache data.

        """
        with open(file_path, 'r') as file:
            data = json.load(file)
        # Convert to OrderedDict to maintain order based on load
        self.memory = OrderedDict(data)
        # Ensure we don't exceed max_size after loading
        while len(self.memory) > self.max_size:
            self.memory.popitem(last=False)

    def export_memory(self, file_path: str) -> None:
        """Exports the current cache data to a JSON file.
        
        Args:
            file_path (str): The path to the file where the cache data will be saved.

        """
        with open(file_path, 'w') as file:
            json.dump(self.memory, file)    