#Copyright 2024 Diego San Andrés Vasco

"""
This file is part of Similator.

Similator is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

Similator is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with Similator. If not, see <https://www.gnu.org/licenses/>.
"""

from typing import Collection, Union

from .memory import Memory
from .valid_data import ValidData

class TextSimilator:
    """A class for comparing text data and optionally caching search results.

    Args:
        valid_data (Union[ValidData, Collection[str], None]): An instance of `ValidData` or a collection of text strings to compare. If a collection of strings is provided, it will automatically be converted into a `ValidData` instance.
        encoding (str): The text encoding. Default is 'utf-8'.
        case_sensitive (bool): Indicates whether the validation should be case-sensitive. Default is True.
        auto_cached (bool): Indicates whether search results should be automatically cached. Default is False.
        max_cache_size (int): The maximum size of the cache if `auto_cached` is True. Default is 100.

    Attributes:
        valid_data (ValidData): An instance of `ValidData` containing the text strings to compare.
        encoding (str): The encoding used for text strings.
        case_sensitive (bool): Indicates whether the validation is case-sensitive.
        auto_cached (bool): Indicates whether search results are automatically cached.
        memory (Memory | None): Instance of the `Memory` class used to store cached results, or `None` if `auto_cached` is False.

    Example:
        >>> valid_strings = ["Hello", "World", "Text", "Example", "Python"]
        >>> valid_data_instance = ValidData(valid_strings, encoding='utf-8')
        >>> text_simulator = TextSimilator(valid_data_instance, encoding='utf-8', case_sensitive=False)
        >>> search_value = "hello"
        >>> results = text_simulator.search(search_value, threshold=0.85)
        >>> results
        [('hello', 2.0)]
        >>> value1 = "hello"
        >>> value2 = "hell"
        >>> similarity_score = text_simulator.compare(value1, value2)
        >>> similarity_score
        1.94
        
    """ 
    def __init__(
            self, 
            valid_data:Union[ValidData, Collection[str], None] = None, 
            encoding:str = 'utf-8', 
            case_sensitive:bool = True,
            auto_cached:bool = False,
            max_cache_size: int = 100
            ) -> None:
        
        self.encoding = encoding
        self.case_sensitive = case_sensitive
        self.auto_cached = auto_cached
        self.memory = Memory(max_size=max_cache_size) if auto_cached else None
        if isinstance(valid_data, ValidData):
            self.valid_data = valid_data
        else:
            self.valid_data = ValidData(valid_data, self.encoding)

    def search(self, value:str, threshold:float = 0.85) -> list:
        """Searches for similar text within the `valid_data` based on the provided `value` and `threshold`.
        
        Parameters:
            `value` (str): The text value to search for.
            `threshold` (float): Similarity threshold for filtering results. Default is `0.85`.

        Returns:
            `list`: A list of tuples containing matched strings and their similarity scores.
        
        Example:
            >>> results = text_simulator.search('hello', threshold=0.85)
            >>> print(results)  # Output: [('hello', 2.0)]

        Raises:
            `EmptyValidData`: If the `valid_data` is empty or not provided.

        """
        from . import _rst_similator
        if self.valid_data.is_empty():
            raise EmptyValidData('Object doesn\'t have values in self.valid_data')
        if not self.case_sensitive:
            value = value.casefold()

        #Check if this search had already been performed and saved in memory and if so, return that result
        cache_key = f'{value}{threshold}'
        if self.auto_cached:
            cached_result = self.memory.get_from_memory(cache_key)
            if cached_result:
                return [(item[0], item[1]) for item in cached_result]
        results = _rst_similator.rst_search(value, self.valid_data.get_data(self.case_sensitive), threshold)
        if self.auto_cached:
            self.memory.add_to_memory(cache_key, results)
        return results
    
    def compare (self, value1:str, value2:str) -> float:
        """Compares two text values and returns a similarity score using Rust-optimized comparison.

        Parameters:
            `value1` (str): The first text value.
            `value2` (str): The second text value.

        Returns:
            `float`: Similarity score between the two text values.
        
        Example:
            >>> similarity_score = text_simulator.compare("hello", "hell")
            >>> print(similarity_score)  # Output: 1.94

        Raises:
            `TypeError`: If either `value1` or `value2` is not a string.

        """
        from . import _rst_similator
        if (not isinstance(value1, str)) or (not isinstance(value2, str)):
            raise TypeError('Values must be strings.')
        if not self.case_sensitive:
            value1, value2 = (value1.casefold(), value2.casefold())
        py_job_str, py_val_str = (value1, value2) if len(value1) <= len(value2) else (value2, value1)

        return _rst_similator.rst_compare(py_job_str, py_val_str)

class EmptyValidData(Exception):
    """Exception raised when `valid_data` is empty or not provided during a search operation."""
    pass