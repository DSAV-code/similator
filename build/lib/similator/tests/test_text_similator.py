#Copyright 2024 Diego San Andrés Vasco

"""
This file is part of Similator.

Similator is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

Similator is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with Similator. If not, see <https://www.gnu.org/licenses/>.
"""
from ..src import TextSimilator, Score, ValidData

def test_text_similator_search():
    valid_strings = ["Hello", "World", "Python", "Programming"]
    valid_data_instance = ValidData(valid_strings, encoding='utf-8', case_sensitive=False)
    text_simulator = TextSimilator(valid_data_instance, encoding='utf-8', case_sensitive=False)
    
    # Look for a value that exists
    search_value = "hello"
    results = text_simulator.search(search_value, threshold=0.5)
    
    assert len(results) == 1
    assert results[0].value == "hello"
    assert isinstance(results[0], Score)

def test_text_similator_compare_exact_match():
    valid_strings = ["Python"]
    text_simulator = TextSimilator(valid_strings, encoding='utf-8', case_sensitive=True)
    
    # Compare two identical strings/bytearrays
    score = text_simulator.compare("Python", "Python")
    second_score = text_simulator.compare(bytearray("Python", text_simulator.encoding), bytearray("Python", text_simulator.encoding))
    assert score == 2.0
    assert second_score == 2.0

def test_text_similator_compare_partial_match():
    valid_strings = ["Programming"]
    text_simulator = TextSimilator(valid_strings, encoding='utf-8', case_sensitive=True)
    
    # Compare two strings/bytearrays with partial match
    score = text_simulator.compare("Program", "Programming")
    second_score = text_simulator.compare(bytearray("Program", text_simulator.encoding), bytearray("Programming", text_simulator.encoding))
    assert 1.0 < score < 2.0
    assert 1.0 < second_score < 2.0

def test_text_similator_compare_case_insensitive():
    valid_strings = ["python"]
    text_simulator = TextSimilator(valid_strings, encoding='utf-8', case_sensitive=False)
    
    # Compare ignoring uppercase/lowercase
    score = text_simulator.compare("Python", "python")
    second_score = text_simulator.compare(bytearray("Python", text_simulator.encoding), bytearray("python", text_simulator.encoding))
    assert score == 2.0
    assert second_score == 2.0