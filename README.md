# jdict

Dictionary extended with convenience methods that depend heavily on dictionaries being ordered by insertion order.

## Requirements

jdict requires Python 3.6+. It will raise an Exception if imported with a lower version.

jdict has no dependencies, except for the following methods which require pandas: `series`, `datarow`, and `datacol`.

## Installation

`pip install jdict`

## Usage

```Python
>>> from jdict import jdict
>>> j = jdict(x=3, y=4, z=5)
>>> j.x
3
>>> j.first
('x', 3)
>>> j.first_key
'x'
>>> j.value_list
[3, 4, 5]
>>> j.list
[('x', 3), ('y', 4), ('z', 5)]
>>> j.last
('z', 5)
>>> j.pop_last()
('z', 5)
>>> j
{'x': 3, 'y': 4}
```

and so on. For more about the usage, see the tests.

## Running tests

Run the following commands

1. `pip install pytest` (if you don't have pytest)
2. `pip install pandas` (if you don't have pandas)
3. `pip install -e .` (if you haven't done so already)
4. `pytest`
