# API Reference

This API reference provides detailed information on the classes, methods, and exceptions available in the **Similator** library.

## `TextSimilator` Class

The `TextSimilator` class provides functionalities for text comparison and searching, integrating high-performance Rust functions. -->

```{eval-rst}
.. autoclass:: similator.TextSimilator
   :members:
   :undoc-members:
   :show-inheritance:
```

---

## `ValidData` Class

The `ValidData` class handles a collection of text strings to be validated and compared.

```{eval-rst}
.. autoclass:: similator.ValidData
   :members:
   :undoc-members:
   :show-inheritance:
```

---

## `Memory` Class

The `Memory` class manages cached search results to optimize repeated searches.

```{eval-rst}
.. autoclass:: similator.Memory
   :members:
   :undoc-members:
   :show-inheritance:
```

---

## Exceptions

### `EmptyValidData`

Exception raised when `valid_data` is empty or not provided during a search operation.

```{eval-rst}
.. autoclass:: similator.text_similator.EmptyValidData
   :members:
   :undoc-members:
   :show-inheritance:
```

---

## Rust Functions Integrated via `_rst_similator`

The following Rust functions are integrated into the `TextSimilator` class for high performance.

### `rst_compare`

Compares two strings for similarity using Rust.

- **Signature:** `rst_compare(job_str: str, val_str: str) -> float`

### `rst_search`

Searches for similar strings within a collection using Rust.

- **Signature:** `rst_search(job_str: str, valid_data: List[str], threshold: float) -> List[Tuple[str, float]]` -->

## Summary

This API reference provides an overview of the available classes, methods, and exceptions in the **Similator** library. For practical examples of how to use these APIs, refer to the [Usage Guide](usage.md).