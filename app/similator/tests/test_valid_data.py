#Copyright 2024 Diego San Andrés Vasco

"""
This file is part of Similator.

Similator is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

Similator is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with Similator. If not, see <https://www.gnu.org/licenses/>.
"""
import pytest
from ..src import ValidData

def test_valid_data_initialization():
    valid_strings = ["Hello", "World", "Python"]
    valid_data_instance = ValidData(valid_strings, encoding='utf-8', case_sensitive=True)
    
    # Verify that the instance is not empty
    assert not valid_data_instance.is_empty()
    
    # Verify that the number of entries is correct
    assert len(valid_data_instance.get_data()) == len(valid_strings)
    
    # Verify that the data conversion is correct
    decoded_data = [data.decode('utf-8') for data in valid_data_instance.get_data()]
    assert set(decoded_data) == set(valid_strings)

def test_case_insensitive_validation():
    valid_strings = ["Hello", "world", "Python"]
    valid_data_instance = ValidData(valid_strings, encoding='utf-8', case_sensitive=False)
    
    # Verify that the validation is not case sensitive
    decoded_data = [data.decode('utf-8') for data in valid_data_instance.get_data()]
    assert "hello" in decoded_data
    assert "world" in decoded_data
    assert "python" in decoded_data


@pytest.mark.parametrize("empty_data", [None, [], "", {}, ()])
def test_empty_initialization(empty_data):
    valid_data_instance = ValidData(empty_data)

    # Verify that an instance with no initial data is empty
    assert valid_data_instance.is_empty()
    assert len(valid_data_instance.get_data()) == 0