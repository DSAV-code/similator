# Usage Guide

This guide provides examples of how to use the **Similator** library for text comparison and validation using the `TextSimilator` class. 

## Initial Setup

To begin using Similator, you need to import the main class and set up some initial data.

### Importing the Necessary Classes

```python
from similator.text_similator import TextSimilator
from similator.valid_data import ValidData
```

### Creating a `ValidData` Instance

The `ValidData` class is used to manage collections of text strings that will be used for comparison and validation.

```python
# Example: Creating a ValidData instance
valid_strings = ["Hello", "World", "Text", "Example", "Python"]
valid_data_instance = ValidData(valid_strings, encoding='utf-8')
```

### Initializing `TextSimilator`

The `TextSimilator` class allows for powerful text comparison and search functionalities. You can initialize it with a `ValidData` instance or directly with a collection of strings.

```python
# Example: Initializing TextSimilator with a ValidData instance
text_simulator = TextSimilator(valid_data_instance, encoding='utf-8', case_sensitive=False)

# Alternatively, initialize it with a collection of strings
text_simulator = TextSimilator(valid_strings, encoding='utf-8', case_sensitive=False)
```

## Text Search with `TextSimilator`

The `search` method allows you to search for similar text within the provided data. You can specify a similarity threshold to control the sensitivity of the search.

```python
# Example: Searching for a text within valid data
search_value = "hello"
results = text_simulator.search(search_value, threshold=0.85)
print(results)  # Output: [('hello', 2.0)]
```

If `auto_cached` is set to `True` during initialization, search results will be cached, improving the performance of repeated searches with the same parameters.

## Text Comparison with `TextSimilator`

The `compare` method provides a similarity score between two strings, leveraging the Rust-optimized function for quick comparisons.

```python
# Example: Comparing two strings
value1 = "hello"
value2 = "hell"
similarity_score = text_simulator.compare(value1, value2)
print(similarity_score)  # Output: 1.94
```

## Using Rust Functions for Performance

The `TextSimilator` class integrates two key Rust functions—`rst_search` and `rst_compare`—to provide optimized performance for text search and comparison. These functions are seamlessly used within the Python class methods, providing a high-performance backend without additional complexity for the user.

```python
from similator._rst_similator import rst_compare, rst_search

valid_strings = ["Hello", "World", "Text", "Example", "Python"]
results = rst_search("Python", valid_strings, threshold=0.85)
print(results)  # Output: [('hello', 2.0)]
```

## Handling Empty Valid Data

If the `ValidData` instance is empty or not provided during a search operation, the `EmptyValidData` exception will be raised.

```python
# Example: Handling empty valid data
try:
    text_simulator = TextSimilator()  # No valid data provided
    text_simulator.search("example")
except EmptyValidData as e:
    print(f"Error: {e}")
```

## Contributing to Similator

We hope you find Similator useful in your projects! 🚀 If you have ideas for improvements, encounter any issues, or want to add new features, we welcome your contributions. Your input and feedback are invaluable to making Similator even better! Check out the [Contribution Guide](contributing.md) to get started and learn how you can help shape the future of this project.

## Summary

The `TextSimilator` class offers powerful and efficient text validation and comparison functionalities by leveraging both Python and Rust. For more details on the API, refer to the [API Reference](api_reference.md) section.