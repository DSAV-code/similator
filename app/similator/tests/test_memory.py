#Copyright 2024 Diego San Andrés Vasco

"""
This file is part of Similator.

Similator is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

Similator is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with Similator. If not, see <https://www.gnu.org/licenses/>.
"""
import pytest
import os
import json
from collections import OrderedDict
from ..src import Memory

@pytest.fixture
def memory():
    return Memory(max_size=3)

def test_add_to_memory(memory):
    # Test adding to memory and checking the content
    memory.add_to_memory("key1", "value1")
    assert memory.get_from_memory("key1") == "value1"

    memory.add_to_memory("key2", "value2")
    memory.add_to_memory("key3", "value3")
    assert len(memory.memory) == 3

    # Test that adding a fourth item removes the oldest one
    memory.add_to_memory("key4", "value4")
    assert memory.get_from_memory("key1") is None
    assert memory.get_from_memory("key2") == "value2"
    assert memory.get_from_memory("key4") == "value4"

def test_get_from_memory(memory):
    # Test retrieval of items
    memory.add_to_memory("key1", "value1")
    memory.add_to_memory("key2", "value2")
    assert memory.get_from_memory("key1") == "value1"
    assert memory.get_from_memory("key2") == "value2"

    # Test retrieval of a non-existent key
    assert memory.get_from_memory("nonexistent") is None

def test_clear_memory(memory):
    # Test clearing the memory
    memory.add_to_memory("key1", "value1")
    memory.add_to_memory("key2", "value2")
    assert len(memory.memory) == 2
    memory.cls()
    assert len(memory.memory) == 0
    assert memory.get_from_memory("key1") is None

def test_load_memory(memory):
    # Test loading memory from a file
    test_data = OrderedDict([("key1", "value1"), ("key2", "value2"), ("key3", "value3")])
    file_path = "test_memory.json"
    with open(file_path, 'w') as file:
        json.dump(test_data, file)

    memory.load_memory(file_path)
    assert len(memory.memory) == 3
    assert memory.get_from_memory("key1") == "value1"

    # Ensure that loading more items than max_size respects the max_size
    test_data["key4"] = "value4"
    with open(file_path, 'w') as file:
        json.dump(test_data, file)

    memory.load_memory(file_path)
    assert len(memory.memory) == 3
    assert memory.get_from_memory("key1") is None  # Oldest item should be removed
    assert memory.get_from_memory("key4") == "value4"

    os.remove(file_path)

def test_export_memory(memory):
    # Test exporting memory to a file
    memory.add_to_memory("key1", "value1")
    memory.add_to_memory("key2", "value2")
    file_path = "test_export_memory.json"

    memory.export_memory(file_path)

    with open(file_path, 'r') as file:
        data = json.load(file)

    expected_data = OrderedDict([("key1", "value1"), ("key2", "value2")])
    assert data == expected_data

    os.remove(file_path)

def test_add_duplicate_key(memory):
    # Test adding a duplicate key updates the value and moves it to the end
    memory.add_to_memory("key1", "value1")
    memory.add_to_memory("key2", "value2")
    memory.add_to_memory("key3", "value3")

    # Add a duplicate key
    memory.add_to_memory("key1", "new_value1")
    
    # Check that "key1" has the updated value and is now the last item
    assert memory.get_from_memory("key1") == "new_value1"
    assert list(memory.memory.keys())[-1] == "key1"