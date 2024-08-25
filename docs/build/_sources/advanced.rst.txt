Advanced Usage
==============

Enabling Caching for Repeated Searches
----------------------------------------

.. code-block:: python

   # Enable caching with a maximum size of 50 cached results
   text_simulator_with_cache = TextSimilator(valid_data_instance, auto_cached=True, max_cache_size=50)

   # Perform a search and it will be cached
   results_cached = text_simulator_with_cache.search("python", threshold=0.9)

Exporting and Loading Cached Data
-----------------------------------

.. code-block:: python

   # Export the current cache to a JSON file
   text_simulator_with_cache.memory.export_memory("cache.json")

   # Load the cache from a JSON file
   text_simulator_with_cache.memory.load_memory("cache.json")

