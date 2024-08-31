#Copyright 2024 Diego San Andrés Vasco

"""
This file is part of Similator.

Similator is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

Similator is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with Similator. If not, see <https://www.gnu.org/licenses/>.
"""
from dataclasses import dataclass, field
from typing import Collection, Union, List

@dataclass(frozen=True, slots=True)
class ValidData:
    """Handles and validates a collection of text data, encoding them for consistent processing.

    Args:
        valid_data (Collection[str] or None): Input strings to be validated and stored. Only first time.
        encoding (str): Character encoding for data processing. Default is 'utf-8'.

    Example:
        >>> valid_strings = ["Hello", "World"]
        >>> valid_data_instance = ValidData(valid_strings, encoding='utf-8')
        >>> valid_data_instance.get_data(case_sensitive=False)
        ['hello', 'world']
        >>> valid_data_instance.is_empty()
        False

    """
    _original_data: Union[Collection[str], None] = None
    encoding: str = 'utf-8'
    __data: List[str] = field(init=False, default_factory=list)

    def __post_init__(self) -> None:
        """Validates and stores data after initialization."""

        object.__setattr__(self, '_ValidData__data', 
                           self._validate_and_transform(self._original_data) if self._original_data else [])

    def _validate_and_transform(self, items_data: Union[Collection[str], List[None]]) -> List[str]:
        """Encodes and deduplicates input strings.

        Args:
            items_data (Collection[str]): Strings to process.

        Returns:
            List[str]: Processed and encoded strings.

        """
        items_data = set(items_data)
        return [value.encode(self.encoding, errors='replace').decode(self.encoding, errors='replace') 
                for value in items_data if isinstance(value, str)]

    def get_data(self, case_sensitive: bool = True) -> List[str]:
        """Retrieves validated data, optionally case-insensitive.

        Args:
            case_sensitive (bool): Return data in original or lowercase form.

        Returns:
            List[str]: Validated strings.

        """
        if case_sensitive:
            return self.__data
        else:
            return [item.casefold() for item in self.__data]

    def is_empty(self) -> bool:
        """Checks if any valid data is stored.

        Returns:
            bool: True if empty, False otherwise.
            
        """
        return len(self.__data) == 0

    def __repr__(self) -> str:
        lenght = len(self.__data)
        if lenght <= 4 and lenght != 1:
            return f"ValidData(valid_data={self.__data} ==> {lenght} items; encoding='{self.encoding}')"
        elif lenght == 1:
            return f"ValidData(valid_data={self.__data} ==> {lenght} item; encoding='{self.encoding}')"
        else:
            return f"ValidData(valid_data=['{self.__data[0]}', '{self.__data[1]}' . . '{self.__data[-2]}', '{self.__data[-1]}'] ==> {lenght} items; encoding='{self.encoding}')"