# jdict

Dictionary extended with convenience methods that depend heavily on dictionaries being ordered by insertion order.

## Requirements

jdict requires Python 3.6+. It will raise an Exception if imported with a lower version.

jdict has no dependencies, except for the following methods which require pandas: `series`, `datarow`, and `datacol`.

## Installation

For now you have to get the source and install with `pip install -e .`

## Usage

In the code:

```Python
from jdict import jdict

x = jdict(x=3, y=2)

# or

x = jdict({'x': 3, 'y': 2})
```

For usage of the JDict instance, see the tests.

## Running tests

Run the following commands

1. `pip install pytest` (if you don't have pytest)
2. `pip install pandas` (if you don't have pandas)
3. `pip install -e .` (if you haven't done so already)
4. `pytest`
