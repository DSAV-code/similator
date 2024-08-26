<div align="center">
  <img src="https://i.imgur.com/mQE6c9Q.png" />
</div>

-----------------

[![Stars](https://img.shields.io/github/stars/DSAV-code/similator?style=social)](https://github.com/DSAV-code/similator)
[![Pypi Version](https://img.shields.io/pypi/v/similator)](https://pypi.org/project/similator)
[![License GPL v3.0](https://img.shields.io/badge/license-GPL%20v3.0-blue.svg)](LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/DSAV-code/similator.svg)](https://github.com/DSAV-code/similator/issues)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-brightgreen.svg)](https://www.python.org/downloads/)
![Tests](https://img.shields.io/github/actions/workflow/status/DSAV-code/similator/run_tests.yml?branch=main)


# Similator: Powerfull Python text validation tool

**Similator** is a powerful Python library designed for efficient text validation and comparison at the byte level. With features like customizable similarity thresholds, case-sensitive or case-insensitive comparisons, and an optional caching mechanism, Similator is ideal for tasks requiring precise text matching and validation.

## 🚀 Features

- **Byte-Level Text Validation and Comparison**: Leverage the power of `bytearrays` for fast and accurate text operations.
- **Customizable Similarity Search**: Set thresholds to find the most relevant matches in your dataset.
- **Automatic Caching**: Enable caching to store and reuse search results, boosting performance in repetitive tasks.
- **Advanced Scoring Mechanism**: A sophisticated scoring system that rewards larger and more significant matches, making your similarity searches more meaningful.
- **Case Sensitivity Options**: Choose between case-sensitive and case-insensitive operations based on your needs.

## 📦 Installation

Install Similator quickly and easily using pip:

```bash
pip install similator
```

## 🌟 Quickstart Guide

Here's a quick example to get you up and running with Similator:

### 1. Import and Initialize

```python
from similator import TextSimilator, ValidData

# Example data
valid_strings = ["Hello", "World", "Text", "Example", "Python"]

# Initialize ValidData
valid_data_instance = ValidData(valid_strings, encoding='utf-8', case_sensitive=False)

# Initialize TextSimilator with ValidData
text_similator = TextSimilator(valid_data_instance, encoding='utf-8', case_sensitive=False)
```

### 2. Perform a Search

Search for a string within the valid data with a similarity threshold:

```python
search_value = "hello"
results = text_similator.search(search_value, threshold=0.85)
print(results)
# Output: [Score(value='hello', points=2.0)]
```

### 3. Compare Two Strings

Directly compare two strings to obtain a similarity score:

```python
value1 = "hello"
value2 = "hell"
similarity_score = text_similator.compare(value1, value2)
print(similarity_score)
# Output: 1.94
```

## Advanced Usage

### Enabling Caching for Repeated Searches

If your application involves repeated searches with similar queries, you can enable caching to improve performance:

```python
# Enable caching with a maximum size of 50 cached results
text_similator_with_cache = TextSimilator(valid_data_instance, auto_cached=True, max_cache_size=50)

# Perform a search and it will be cached
results_cached = text_similator_with_cache.search("python", threshold=0.9)
```

### Exporting and Loading Cached Data

You can export the cache to a file and reload it later for persistent storage:

```python
# Export the current cache to a JSON file
text_similator_with_cache.memory.export_memory("cache.json")

# Load the cache from a JSON file
text_similator_with_cache.memory.load_memory("cache.json")
```

---

## 💬 Contact

If you have any questions, suggestions, or just want to say hello, feel free to contact me:

- **Email**: sanandresvascodiego@gmail.com
- **GitHub**: [DSAV-code](https://github.com/DSAV-code)
- **Twitter/X**: [@dsav_v2](https://twitter.com/dsav_v2)

## 🛠️ Contributing

Contributions are welcome! If you have any ideas, suggestions, or issues, feel free to open an issue or submit a pull request.

## 📝 License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

---
