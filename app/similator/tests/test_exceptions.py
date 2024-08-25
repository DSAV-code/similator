#Copyright 2024 Diego San Andrés Vasco

"""
This file is part of Similator.

Similator is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

Similator is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with Similator. If not, see <https://www.gnu.org/licenses/>.
"""
import pytest
from app.src import ValidData, TextSimilator, EmptyValidData, Memory

def test_empty_valid_data_exception():
    empty_data_instance = ValidData([])
    text_simulator = TextSimilator(empty_data_instance)
    
    # Verify that the appropriate exception is thrown when there is no valid data
    with pytest.raises(EmptyValidData):
        text_simulator.search("Hello")

def test_initialization_with_invalid_max_size():
    # Test initializing Memory with an invalid max_size
    with pytest.raises(ValueError):
        Memory(max_size=-1)
    with pytest.raises(TypeError):
        Memory(max_size='strdata')