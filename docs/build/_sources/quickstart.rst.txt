Quickstart
==========

Here's a quick example to get you up and running with Similator:

Import and Initialize
----------------------

.. code-block:: python

   from similator import TextSimilator, ValidData

   # Example data
   valid_strings = ["Hello", "World", "Text", "Example", "Python"]

   # Initialize ValidData
   valid_data_instance = ValidData(valid_strings, encoding='utf-8', case_sensitive=False)

   # Initialize TextSimilator with ValidData
   text_simulator = TextSimilator(valid_data_instance, encoding='utf-8', case_sensitive=False)

Perform a Search
-----------------

.. code-block:: python

   search_value = "hello"
   results = text_simulator.search(search_value, threshold=0.85)
   print(results)
   # Output: [Score(value='hello', points=2.0)]

Compare Two Strings
--------------------

.. code-block:: python

   value1 = "hello"
   value2 = "hell"
   similarity_score = text_simulator.compare(value1, value2)
   print(similarity_score)
   # Output: 1.94

