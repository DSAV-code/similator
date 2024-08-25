#Copyright 2024 Diego San Andrés Vasco

"""
This file is part of Similator.

Similator is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

Similator is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with Similator. If not, see <https://www.gnu.org/licenses/>.
"""

from typing import Collection, NoReturn, Union, List

class ValidData:
    """
    A class for handling and validating a collection of text strings by converting them to bytearrays.

    Args:
        valid_data (Union[Collection[str],None]): A collection of valid text strings to validate and convert.
        encoding (str): The text encoding. Default is 'utf-8'.
        case_sensitive (bool): Determines if the validation is case-sensitive. Default is True.
    
    Attributes:
        encoding (str): The encoding used for text strings.
        case_sensitive (bool): Indicates whether the validation is case-sensitive.
        __data (List[bytearray]): A collection of validated values transformed into bytearrays.

    Example:
        >>> valid_strings = ["Hello", "World", "Text", "Example", "Python"]
        >>> valid_data_instance = ValidData(valid_strings, encoding='utf-8', case_sensitive=False)
        >>> validated_data = valid_data_instance.get_data()
        >>> [data.decode('utf-8') for data in validated_data]
        ['hello', 'world', 'text', 'example', 'python']
        >>> valid_data_instance.is_empty()
        False
    """

    def __init__(self, valid_data: Union[Collection[str],None] = None, encoding: str = 'utf-8', case_sensitive: bool = True) -> None:
        self.encoding = encoding
        self.case_sensitive = case_sensitive
        self.__data = self._validate_and_transform(valid_data) if valid_data else []

    def _validate_and_transform(self, valid_data: Union[Collection[str],List[NoReturn]]) -> List[bytearray]:
        """
        Validates the provided text strings and transforms them into bytearrays.

        Args:
            valid_data (Collection[str]|List[NoReturn]): A collection of valid text strings.

        Returns:
            List[bytearray]: A list of validated and transformed bytearrays.
        """
        if not self.case_sensitive:
            valid_data = set(value.casefold() for value in valid_data if value)
        else:
            valid_data = set(valid_data)

        return [bytearray(value, self.encoding) for value in valid_data if value]

    def get_data(self) -> List[bytearray]:
        """
        Returns the validated and transformed bytearrays.

        Returns:
            List[bytearray]: A list of validated and transformed bytearrays.
        """
        return self.__data

    def is_empty(self) -> bool:
        """
        Checks if the validated data is empty.

        Returns:
            bool: True if no valid data is present, False otherwise.
        """
        return len(self.__data) == 0