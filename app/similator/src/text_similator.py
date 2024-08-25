#Copyright 2024 Diego San Andrés Vasco

"""
This file is part of Similator.

Similator is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

Similator is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with Similator. If not, see <https://www.gnu.org/licenses/>.
"""

from collections import namedtuple
from operator import attrgetter
from typing import Collection, Generator, Union, List, NoReturn
from .memory import Memory
from .valid_data import ValidData

Score = namedtuple('Score', ['value', 'points'])
Position = namedtuple('Position', ['arr1', 'arr2', 'win_size'])

class TextSimilator:
    """
    A class for comparing text data using bytearrays and optionally caching search results.

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
        >>> valid_data_instance = ValidData(valid_strings, encoding='utf-8', case_sensitive=False)
        >>> text_simulator = TextSimilator(valid_data_instance, encoding='utf-8', case_sensitive=False)
        >>> search_value = "hello"
        >>> results = text_simulator.search(search_value, threshold=0.85)
        >>> results
        [Score(value='hello', points=2.0)]
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
        if isinstance(valid_data, ValidData): self.valid_data = valid_data
        else: self.valid_data = ValidData(valid_data, self.encoding, self.case_sensitive)

    def search(self, value:str, threshold:float = 0.85) -> list:
        """
        Searches for matches in `valid_data` with the provided value based on a similarity threshold.
        
        If `auto_cached` is enabled, it first checks the cache for previous results. If the search has been performed before, the cached result is returned. If not, the search is performed, and the result is then cached for future use.

        Args:
            value (str): The value to search for.
            threshold (float): The minimum score threshold to consider a match. Default is 0.85.

        Returns:
            list: A list of `Score` objects sorted by `points` in descending order.

        Raises:
            EmptyValidData: If `valid_data` is empty or not defined.
        """
        if self.valid_data.is_empty(): raise EmptyValidData('Object doesn\'t have values in self.valid_data')
        if not self.case_sensitive: value = value.casefold()

        #Check if this search had already been performed and saved in memory and if so, return that result
        cache_key = f'{value}{threshold}'
        if self.auto_cached:
            cached_result = self.memory.get_from_memory(cache_key)
            if cached_result: return [Score(value=item[0], points=item[1]) for item in cached_result]
        
        results_list = []
        
        for val_arr in self.valid_data.get_data():
            job_arr = bytearray(value.strip(), self.encoding)
            points = self.compare(job_arr, val_arr, second_was_validated=True)

            if points >= threshold:
                results_list.append(Score(value=val_arr.decode(self.encoding), points=points))
        
        sorted_results = sorted(results_list, key=attrgetter('points'), reverse=True) 
        if self.auto_cached:
            self.memory.add_to_memory(cache_key, sorted_results)
        
        return sorted_results
    
    def compare (self, value1:Union[str, bytearray], value2:Union[str, bytearray], second_was_validated:bool = False):
        """
        Compares two text values and returns a similarity score.

        Args:
            value1 (str|bytearray): The first value to compare.
            value2 (str|bytearray): The second value to compare.
            second_was_validated (bool): Indicates whether `value2` is assumed to be the correct value. 
                                         This affects how the comparison is performed and points are calculated. Default is False.

        Returns:
            float: The similarity score between `value1` and `value2`.
        """
        if not self.case_sensitive:
            if isinstance(value1, str): value1 = value1.casefold()
            elif isinstance(value1, bytearray) and (not second_was_validated): value1 = bytearray(value1.decode(self.encoding).casefold(), self.encoding)
            if isinstance(value2, str): value2 = value2.casefold()
            elif isinstance(value2, bytearray) and (not second_was_validated): value2 = bytearray(value2.decode(self.encoding).casefold(), self.encoding)
        
        if not isinstance(value1, bytearray): value1 = bytearray(value1.strip(), self.encoding)
        if not isinstance(value2, bytearray): value2 = bytearray(value2.strip(), self.encoding)
        if second_was_validated:
            job_arr = value1.copy()
            val_arr = value2.copy()
            tmpl_arr = bytearray('~' * len(val_arr), self.encoding)
        else: 
            short, long = (value1, value2) if len(value1) <= len(value2) else (value2, value1)
            job_arr = short.copy()
            val_arr = long.copy() 
            tmpl_arr = bytearray('~' * len(val_arr), self.encoding)
        
        coincidences_plus = 0
        original_size = len(job_arr)
        window_size = min(len(job_arr), len(val_arr))
        finished = False

        while not finished:
            match_list = self.__get_positions(job_arr, val_arr, window_size)
            if window_size <= 2:
                finished = True
                break
            
            if not match_list:
                window_size -= 1
                continue
            
            mask = self.__mask_array(len(job_arr), match_list)
            job_arr = bytearray([byte for byte, mask_value in zip(job_arr, mask) if mask_value])

            # Complete template
            for pos in match_list:
                coincidences_plus += pos.win_size**2
                tmpl_arr[pos.arr2:pos.arr2 + pos.win_size] = val_arr[pos.arr2:pos.arr2 + pos.win_size]

            # Check if finished
            if b'~' not in tmpl_arr or len(job_arr) == 0:
                finished = True
                break
            else:
                window_size = min((len(tmpl_arr) - tmpl_arr.count(b'~')), len(job_arr))

        points = self.__calculate_score(tmpl_arr, job_arr, original_size, coincidences_plus)
        return points

    
    def __get_positions(self, array1:bytearray, array2:bytearray, window_size:int) -> Union[List[Position],List[NoReturn]]:
        """
        Finds the positions where there are matches between two `bytearrays` using a sliding window.

        Args:
            array1 (bytearray): The first `bytearray`.
            array2 (bytearray): The second `bytearray`.
            window_size (int): The size of the sliding window.

        Returns:
            List[Position]: A list of matching positions.
        """
        position_list = []
        for array1_index, array1_window in enumerate(self.__sliding_window(array1, window_size)):
            for array2_index, array2_window in enumerate(self.__sliding_window(array2, window_size)):
                if array1_window == array2_window: 
                    position_list.append(Position(arr1=array1_index, arr2=array2_index, win_size=window_size))
        return position_list
    
    @classmethod
    def __mask_array(cls, array_size:int, matchs_list:List[Position]) -> List[bool]:
        """
        Generates a mask for a `bytearray` based on the found matches.

        Args:
            array_size (int): The size of the `bytearray`.
            matchs_list (List[Position]): A list of matching positions.

        Returns:
            List[bool]: Generates a mask for a `bytearray` based on the found matches, where True indicates a non-matching position and False indicates a matching one.
        """
        mask = [True] * array_size
        for position in matchs_list:
            mask[position.arr1:position.arr1 + position.win_size] = [False] * position.win_size
        return mask
    
    @classmethod
    def __sliding_window(cls, arr: bytearray, window_size: int) -> Generator:
        """
        Creates a sliding window over a `bytearray`.

        Args:
            arr (bytearray): The `bytearray` over which the window will slide.
            window_size (int): The size of the window.

        Returns:
            Generator: A generator of `bytearray` windows.

        Raises:
            ValueError: If the window size is greater than the `bytearray` length.
        """
        if window_size > len(arr):
            raise ValueError(f"The window size ({window_size}) can't be greater than the `bytearray` length ({len(arr)}).")
        return (arr[i:i + window_size] for i in range(len(arr) - window_size + 1))
    
    @classmethod
    def __calculate_score(cls, tmpl_arr: bytearray, job_arr: bytearray, original_size:int, plus:int) -> float:
        """
        Calculates the final score based on matches and discrepancies.

        Args:
            tmpl_arr (bytearray): The template with the found matches.
            job_arr (bytearray): The `bytearray` with the non-matching positions.
            original_size (int): The original size of the `bytearray`.
            plus (int): The sum of the squares of the sizes of the found matches. This rewards matches with larger sizes.

        Returns:
            float: The final similarity score.
        """
        coincidences = len(tmpl_arr) - (discrepancies:= tmpl_arr.count(b'~'))
        coincidences += (plus/original_size)
        discrepancies += len(job_arr)
        final_score = round((coincidences - (discrepancies/min(len(tmpl_arr), original_size)))/min(len(tmpl_arr), original_size), 2)
        return final_score if final_score >= 0 else 0.0

class EmptyValidData(Exception):
    """Exception raised when `valid_data` is empty or not provided during a search operation."""
    pass