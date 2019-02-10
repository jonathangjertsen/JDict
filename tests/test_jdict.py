import pandas as pd
import pytest

from jdict import JDict

@pytest.fixture
def in_data():
	return {'x': 3, 'y': 4, 'z': 5}

@pytest.fixture
def jdict(in_data):
	return JDict(in_data)

@pytest.fixture
def empty_jdict():
	return JDict()

@pytest.fixture
def empty_jdict_from_empty_jdict_dict():
	return JDict({})

def test_construct(in_data, empty_jdict, empty_jdict_from_empty_jdict_dict, jdict):
	assert len(empty_jdict) == 0
	assert len(empty_jdict_from_empty_jdict_dict) == 0
	assert len(jdict) == 3
	assert(empty_jdict.data == {})
	assert(empty_jdict_from_empty_jdict_dict.data == {})
	assert jdict.data == in_data
	assert jdict.data is in_data

def test_getattr(empty_jdict, jdict):
	with pytest.raises(AttributeError):
		empty_jdict.x

	assert jdict.x == jdict['x']
	jdict['x'] = 1000
	assert jdict.x == 1000

	with pytest.raises(AttributeError):
		jdict.w

def test_setattr(empty_jdict, jdict):
	with pytest.raises(AttributeError):
		empty_jdict.x

	jdict.x = 1000
	assert jdict.x == 1000
	assert jdict['x'] == 1000

	jdict.w = 1000
	assert jdict.w == 1000
	assert jdict['w'] == 1000

def test_keylist(empty_jdict, jdict):
	assert empty_jdict.keylist == []
	assert jdict.keylist == ['x', 'y', 'z']

def test_valuelist(empty_jdict, jdict):
	assert empty_jdict.valuelist == []
	assert jdict.valuelist == [3, 4, 5]

def test_itemlist(empty_jdict, jdict):
	assert empty_jdict.itemlist == []
	assert jdict.itemlist == [('x', 3), ('y', 4), ('z', 5)]

def test_firstitem(empty_jdict, jdict):
	assert empty_jdict.firstitem is None
	assert jdict.firstitem == ('x', 3)

def test_firstkey(empty_jdict, jdict):
	assert empty_jdict.firstkey is None
	assert jdict.firstkey == 'x'

def test_firstvalue(empty_jdict, jdict):
	assert empty_jdict.firstvalue is None
	assert jdict.firstvalue == 3

def test_lastitem(empty_jdict, jdict):
	assert empty_jdict.lastitem is None
	assert jdict.lastitem == ('z', 5)

def test_lastkey(empty_jdict, jdict):
	assert empty_jdict.lastkey is None
	assert jdict.lastkey == 'z'

def test_lastvalue(empty_jdict, jdict):
	assert empty_jdict.lastvalue is None
	assert jdict.lastvalue == 5

def test_anyitem(empty_jdict, jdict):
	assert empty_jdict.anyitem is None
	assert jdict.anyitem is not None
	assert len(jdict.anyitem) == 2

def test_anykey(empty_jdict, jdict):
	assert empty_jdict.anykey is None
	assert jdict.anykey is not None
	assert type(jdict.anykey) is str

def test_anyvalue(empty_jdict, jdict):
	assert empty_jdict.anyvalue is None
	assert jdict.anyvalue is not None
	assert type(jdict.anyvalue) is int

def test_range(empty_jdict, jdict):
	assert type(empty_jdict.range) is range
	assert type(jdict.range) is range
	assert len(empty_jdict.range) == 0
	assert len(jdict.range) == 3
	assert list(empty_jdict.range) == []
	assert list(jdict.range) == [0,1,2]

def test_enumkeys(empty_jdict, jdict):
	assert type(empty_jdict.enumkeys) is enumerate
	assert type(jdict.enumkeys) is enumerate
	assert list(empty_jdict.enumkeys) == []
	assert list(jdict.enumkeys) == [(0, 'x'), (1, 'y'), (2, 'z')]

def test_enumvalues(empty_jdict, jdict):
	assert type(empty_jdict.enumvalues) is enumerate
	assert type(jdict.enumvalues) is enumerate
	assert list(empty_jdict.enumvalues) == []
	assert list(jdict.enumvalues) == [(0, 3), (1, 4), (2, 5)]

def test_enumitems(empty_jdict, jdict):
	assert type(empty_jdict.enumitems) is zip
	assert type(jdict.enumitems) is zip
	assert list(empty_jdict.enumitems) == []
	assert list(jdict.enumitems) == [(0, 'x', 3), (1, 'y', 4), (2, 'z', 5)]

def test_json(empty_jdict, jdict):
	assert empty_jdict.json == '{}'
	assert jdict.json == '{"x": 3, "y": 4, "z": 5}'

def test_series(empty_jdict, jdict):
	assert isinstance(empty_jdict.series, pd.Series)
	assert isinstance(jdict.series, pd.Series)
	assert len(empty_jdict.series) == 0
	assert len(jdict.series) == 3
	assert list(jdict.series.index) == ['x', 'y', 'z']
	assert list(jdict.series) == [3, 4, 5]

def test_datacol(empty_jdict, jdict):
	assert isinstance(empty_jdict.datacol, pd.DataFrame)
	assert isinstance(jdict.datacol, pd.DataFrame)
	assert len(empty_jdict.datacol) == 0
	assert len(jdict.datacol) == 3
	assert list(jdict.datacol.index) == ['x', 'y', 'z']
	assert list(jdict.datacol[0]) == [3, 4, 5]

def test_datarow(empty_jdict, jdict):
	assert isinstance(empty_jdict.datarow, pd.DataFrame)
	assert isinstance(jdict.datarow, pd.DataFrame)
	assert len(empty_jdict.datarow) == 1
	assert len(jdict.datarow) == 1
	assert list(jdict.datarow.index) == [0]
	assert list(jdict.datarow['x']) == [3]
	assert list(jdict.datarow['y']) == [4]
	assert list(jdict.datarow['z']) == [5]

def test_at(empty_jdict, jdict):
	assert jdict.at(0) == ('x', 3)
	assert jdict.at(1) == ('y', 4)
	assert jdict.at(2) == ('z', 5)

	with pytest.raises(IndexError):
		empty_jdict.at(0)
	with pytest.raises(IndexError):
		empty_jdict.at(1)
	with pytest.raises(IndexError):
		jdict.at(-1)
	with pytest.raises(IndexError):
		jdict.at(3)


def test_key_at(empty_jdict, jdict):
	assert jdict.key_at(0) == 'x'
	assert jdict.key_at(1) == 'y'
	assert jdict.key_at(2) == 'z'

	with pytest.raises(IndexError):
		empty_jdict.key_at(0)
	with pytest.raises(IndexError):
		empty_jdict.key_at(1)
	with pytest.raises(IndexError):
		jdict.key_at(-1)
	with pytest.raises(IndexError):
		jdict.key_at(3)


def test_value_at(empty_jdict, jdict):
	assert jdict.value_at(0) == 3
	assert jdict.value_at(1) == 4
	assert jdict.value_at(2) == 5

	with pytest.raises(IndexError):
		empty_jdict.value_at(0)
	with pytest.raises(IndexError):
		empty_jdict.value_at(1)
	with pytest.raises(IndexError):
		jdict.value_at(-1)
	with pytest.raises(IndexError):
		jdict.value_at(3)

def test_pop_first(empty_jdict, jdict):
	with pytest.raises(IndexError):
		empty_jdict.pop_first()

	v0 = jdict.pop_first()
	len0 = len(jdict)
	v1 = jdict.pop_first()
	len1 = len(jdict)
	v2 = jdict.pop_first()
	len2 = len(jdict)

	with pytest.raises(IndexError):
		jdict.pop_first()
	
	assert v0 == ('x', 3)
	assert v1 == ('y', 4)
	assert v2 == ('z', 5)
	assert len0 == 2
	assert len1 == 1
	assert len2 == 0

def test_pop_last(empty_jdict, jdict):
	with pytest.raises(IndexError):
		empty_jdict.pop_last()

	v0 = jdict.pop_last()
	len0 = len(jdict)
	v1 = jdict.pop_last()
	len1 = len(jdict)
	v2 = jdict.pop_last()
	len2 = len(jdict)

	with pytest.raises(IndexError):
		jdict.pop_last()
	
	assert v0 == ('z', 5)
	assert v1 == ('y', 4)
	assert v2 == ('x', 3)
	assert len0 == 2
	assert len1 == 1
	assert len2 == 0

def test_pop_first_key(empty_jdict, jdict):
	with pytest.raises(IndexError):
		empty_jdict.pop_first_key()

	v0 = jdict.pop_first_key()
	len0 = len(jdict)
	v1 = jdict.pop_first_key()
	len1 = len(jdict)
	v2 = jdict.pop_first_key()
	len2 = len(jdict)

	with pytest.raises(IndexError):
		jdict.pop_first_key()
	
	assert v0 == 'x'
	assert v1 == 'y'
	assert v2 == 'z'
	assert len0 == 2
	assert len1 == 1
	assert len2 == 0

def test_pop_first_value(empty_jdict, jdict):
	with pytest.raises(IndexError):
		empty_jdict.pop_first_value()

	v0 = jdict.pop_first_value()
	len0 = len(jdict)
	v1 = jdict.pop_first_value()
	len1 = len(jdict)
	v2 = jdict.pop_first_value()
	len2 = len(jdict)

	with pytest.raises(IndexError):
		jdict.pop_first_value()
	
	assert v0 == 3
	assert v1 == 4
	assert v2 == 5
	assert len0 == 2
	assert len1 == 1
	assert len2 == 0

def test_pop_last_key(empty_jdict, jdict):
	with pytest.raises(IndexError):
		empty_jdict.pop_last_key()

	v0 = jdict.pop_last_key()
	len0 = len(jdict)
	v1 = jdict.pop_last_key()
	len1 = len(jdict)
	v2 = jdict.pop_last_key()
	len2 = len(jdict)

	with pytest.raises(IndexError):
		jdict.pop_last_key()
	
	assert v0 == 'z'
	assert v1 == 'y'
	assert v2 == 'x'
	assert len0 == 2
	assert len1 == 1
	assert len2 == 0

def test_pop_last_value(empty_jdict, jdict):
	with pytest.raises(IndexError):
		empty_jdict.pop_last_value()

	v0 = jdict.pop_last_value()
	len0 = len(jdict)
	v1 = jdict.pop_last_value()
	len1 = len(jdict)
	v2 = jdict.pop_last_value()
	len2 = len(jdict)

	with pytest.raises(IndexError):
		jdict.pop_last_value()
	
	assert v0 == 5
	assert v1 == 4
	assert v2 == 3
	assert len0 == 2
	assert len1 == 1
	assert len2 == 0
