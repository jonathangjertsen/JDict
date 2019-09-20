import pandas as pd
import pytest

from jdict import jdict


@pytest.fixture
def in_data():
    return {"x": 3, "y": 4, "z": 5}


@pytest.fixture
def nonempty(in_data):
    return jdict(in_data)


@pytest.fixture
def empty():
    return jdict()


def test_constructors(in_data):
    empty = jdict()
    empty_from_empty_dict = jdict({})
    nonempty_from_dict = jdict(in_data)
    nonempty_from_kwargs = jdict(x=3, y=4, z=5)

    assert len(empty) == 0
    assert len(empty_from_empty_dict) == 0
    assert len(nonempty_from_dict) == 3
    assert len(nonempty_from_kwargs) == 3
    assert empty.data == {}
    assert empty_from_empty_dict.data == {}
    assert nonempty_from_dict.data == in_data
    assert nonempty_from_kwargs.data == in_data
    assert nonempty_from_dict.data == in_data
    assert nonempty_from_kwargs.data == in_data
    assert nonempty_from_dict.data is in_data


def test_special_case_data_kwarg(in_data):
    assert jdict(**in_data, data="whoops!") == {**in_data, "data": "whoops!"}


def test_special_case_data_positional(in_data):
    assert jdict("whoops!") == {"data": "whoops!"}


def test_getattr(empty, nonempty):
    with pytest.raises(AttributeError):
        empty.x

    assert nonempty.x == nonempty["x"]
    nonempty["x"] = 1000
    assert nonempty.x == 1000

    with pytest.raises(AttributeError):
        nonempty.w


def test_setattr(empty, nonempty):
    with pytest.raises(AttributeError):
        empty.x

    nonempty.x = 1000
    assert nonempty.x == 1000
    assert nonempty["x"] == 1000

    nonempty.w = 1000
    assert nonempty.w == 1000
    assert nonempty["w"] == 1000


def test_list(empty, nonempty):
    assert empty.list == []
    assert nonempty.list == [("x", 3), ("y", 4), ("z", 5)]


def test_key_list(empty, nonempty):
    assert empty.key_list == []
    assert nonempty.key_list == ["x", "y", "z"]


def test_value_list(empty, nonempty):
    assert empty.value_list == []
    assert nonempty.value_list == [3, 4, 5]


def test_first(empty, nonempty):
    assert empty.first is None
    assert nonempty.first == ("x", 3)


def test_first_key(empty, nonempty):
    assert empty.first_key is None
    assert nonempty.first_key == "x"


def test_first_value(empty, nonempty):
    assert empty.first_value is None
    assert nonempty.first_value == 3


def test_last(empty, nonempty):
    assert empty.last is None
    assert nonempty.last == ("z", 5)


def test_last_key(empty, nonempty):
    assert empty.last_key is None
    assert nonempty.last_key == "z"


def test_last_value(empty, nonempty):
    assert empty.last_value is None
    assert nonempty.last_value == 5


def test_any(empty, nonempty):
    assert empty.any is None
    assert nonempty.any is not None
    assert len(nonempty.any) == 2


def test_any_key(empty, nonempty):
    assert empty.any_key is None
    assert nonempty.any_key is not None
    assert type(nonempty.any_key) is str


def test_any_value(empty, nonempty):
    assert empty.any_value is None
    assert nonempty.any_value is not None
    assert type(nonempty.any_value) is int


def test_range(empty, nonempty):
    assert type(empty.range) is range
    assert type(nonempty.range) is range
    assert len(empty.range) == 0
    assert len(nonempty.range) == 3
    assert list(empty.range) == []
    assert list(nonempty.range) == [0, 1, 2]


def test_enum_keys(empty, nonempty):
    assert type(empty.enum_keys) is enumerate
    assert type(nonempty.enum_keys) is enumerate
    assert list(empty.enum_keys) == []
    assert list(nonempty.enum_keys) == [(0, "x"), (1, "y"), (2, "z")]


def test_enum_values(empty, nonempty):
    assert type(empty.enum_values) is enumerate
    assert type(nonempty.enum_values) is enumerate
    assert list(empty.enum_values) == []
    assert list(nonempty.enum_values) == [(0, 3), (1, 4), (2, 5)]


def test_enum(empty, nonempty):
    assert type(empty.enum) is zip
    assert type(nonempty.enum) is zip
    assert list(empty.enum) == []
    assert list(nonempty.enum) == [(0, "x", 3), (1, "y", 4), (2, "z", 5)]


def test_json(empty, nonempty):
    assert empty.json == "{}"
    assert nonempty.json == '{"x": 3, "y": 4, "z": 5}'


def test_series(empty, nonempty):
    assert isinstance(empty.series, pd.Series)
    assert isinstance(nonempty.series, pd.Series)
    assert len(empty.series) == 0
    assert len(nonempty.series) == 3
    assert list(nonempty.series.index) == ["x", "y", "z"]
    assert list(nonempty.series) == [3, 4, 5]


def test_datacol(empty, nonempty):
    assert isinstance(empty.datacol, pd.DataFrame)
    assert isinstance(nonempty.datacol, pd.DataFrame)
    assert len(empty.datacol) == 0
    assert len(nonempty.datacol) == 3
    assert list(nonempty.datacol.index) == ["x", "y", "z"]
    assert list(nonempty.datacol[0]) == [3, 4, 5]


def test_datarow(empty, nonempty):
    assert isinstance(empty.datarow, pd.DataFrame)
    assert isinstance(nonempty.datarow, pd.DataFrame)
    assert len(empty.datarow) == 1
    assert len(nonempty.datarow) == 1
    assert list(nonempty.datarow.index) == [0]
    assert list(nonempty.datarow["x"]) == [3]
    assert list(nonempty.datarow["y"]) == [4]
    assert list(nonempty.datarow["z"]) == [5]


def test_at(empty, nonempty):
    assert nonempty.at(0) == ("x", 3)
    assert nonempty.at(1) == ("y", 4)
    assert nonempty.at(2) == ("z", 5)

    with pytest.raises(IndexError):
        empty.at(0)
    with pytest.raises(IndexError):
        empty.at(1)
    with pytest.raises(IndexError):
        nonempty.at(-1)
    with pytest.raises(IndexError):
        nonempty.at(3)


def test_key_at(empty, nonempty):
    assert nonempty.key_at(0) == "x"
    assert nonempty.key_at(1) == "y"
    assert nonempty.key_at(2) == "z"

    with pytest.raises(IndexError):
        empty.key_at(0)
    with pytest.raises(IndexError):
        empty.key_at(1)
    with pytest.raises(IndexError):
        nonempty.key_at(-1)
    with pytest.raises(IndexError):
        nonempty.key_at(3)


def test_value_at(empty, nonempty):
    assert nonempty.value_at(0) == 3
    assert nonempty.value_at(1) == 4
    assert nonempty.value_at(2) == 5

    with pytest.raises(IndexError):
        empty.value_at(0)
    with pytest.raises(IndexError):
        empty.value_at(1)
    with pytest.raises(IndexError):
        nonempty.value_at(-1)
    with pytest.raises(IndexError):
        nonempty.value_at(3)


def test_pop_first(empty, nonempty):
    with pytest.raises(IndexError):
        empty.pop_first()

    v0 = nonempty.pop_first()
    len0 = len(nonempty)
    v1 = nonempty.pop_first()
    len1 = len(nonempty)
    v2 = nonempty.pop_first()
    len2 = len(nonempty)

    with pytest.raises(IndexError):
        nonempty.pop_first()

    assert v0 == ("x", 3)
    assert v1 == ("y", 4)
    assert v2 == ("z", 5)
    assert len0 == 2
    assert len1 == 1
    assert len2 == 0


def test_pop_last(empty, nonempty):
    with pytest.raises(IndexError):
        empty.pop_last()

    v0 = nonempty.pop_last()
    len0 = len(nonempty)
    v1 = nonempty.pop_last()
    len1 = len(nonempty)
    v2 = nonempty.pop_last()
    len2 = len(nonempty)

    with pytest.raises(IndexError):
        nonempty.pop_last()

    assert v0 == ("z", 5)
    assert v1 == ("y", 4)
    assert v2 == ("x", 3)
    assert len0 == 2
    assert len1 == 1
    assert len2 == 0


def test_pop_first_key(empty, nonempty):
    with pytest.raises(IndexError):
        empty.pop_first_key()

    v0 = nonempty.pop_first_key()
    len0 = len(nonempty)
    v1 = nonempty.pop_first_key()
    len1 = len(nonempty)
    v2 = nonempty.pop_first_key()
    len2 = len(nonempty)

    with pytest.raises(IndexError):
        nonempty.pop_first_key()

    assert v0 == "x"
    assert v1 == "y"
    assert v2 == "z"
    assert len0 == 2
    assert len1 == 1
    assert len2 == 0


def test_pop_first_value(empty, nonempty):
    with pytest.raises(IndexError):
        empty.pop_first_value()

    v0 = nonempty.pop_first_value()
    len0 = len(nonempty)
    v1 = nonempty.pop_first_value()
    len1 = len(nonempty)
    v2 = nonempty.pop_first_value()
    len2 = len(nonempty)

    with pytest.raises(IndexError):
        nonempty.pop_first_value()

    assert v0 == 3
    assert v1 == 4
    assert v2 == 5
    assert len0 == 2
    assert len1 == 1
    assert len2 == 0


def test_pop_last_key(empty, nonempty):
    with pytest.raises(IndexError):
        empty.pop_last_key()

    v0 = nonempty.pop_last_key()
    len0 = len(nonempty)
    v1 = nonempty.pop_last_key()
    len1 = len(nonempty)
    v2 = nonempty.pop_last_key()
    len2 = len(nonempty)

    with pytest.raises(IndexError):
        nonempty.pop_last_key()

    assert v0 == "z"
    assert v1 == "y"
    assert v2 == "x"
    assert len0 == 2
    assert len1 == 1
    assert len2 == 0


def test_pop_last_value(empty, nonempty):
    with pytest.raises(IndexError):
        empty.pop_last_value()

    v0 = nonempty.pop_last_value()
    len0 = len(nonempty)
    v1 = nonempty.pop_last_value()
    len1 = len(nonempty)
    v2 = nonempty.pop_last_value()
    len2 = len(nonempty)

    with pytest.raises(IndexError):
        nonempty.pop_last_value()

    assert v0 == 5
    assert v1 == 4
    assert v2 == 3
    assert len0 == 2
    assert len1 == 1
    assert len2 == 0


def test_add():
    a = jdict(x=3, y=4, z=5)
    b = jdict(a=3, b=4, c=5)
    assert a + b == b + a == jdict(a=3, b=4, c=5, x=3, y=4, z=5)


def test_iadd():
    a = jdict(x=3, y=4, z=5)
    a += jdict(a=3, b=4, c=5)
    assert a == jdict(a=3, b=4, c=5, x=3, y=4, z=5)


def test_mapping():
    assert jdict(x=3, y=4, z=5).mapping(
        key_func=lambda k: k * 2, value_func=lambda v: v * 3
    ) == jdict(xx=9, yy=12, zz=15)


def test_item_mapping():
    assert jdict(x=3, y=4, z=5).item_mapping(lambda k, v: (k * 2, v * 3)) == jdict(
        xx=9, yy=12, zz=15
    )


def test_key_mapping():
    assert jdict(x=3, y=4, z=5).key_mapping(lambda k: k * 2) == jdict(xx=3, yy=4, zz=5)


def test_value_mapping():
    assert jdict(x=3, y=4, z=5).value_mapping(lambda v: v * 3) == jdict(x=9, y=12, z=15)


def test_select():
    assert jdict(x=3, y=4, z=5).select(
        key_func=lambda k: k in ("x", "y"), value_func=lambda v: v != 4
    ) == jdict(x=3)


def test_item_select():
    assert jdict(x=3, y=4, z=5).item_select(
        lambda k, v: (k in ("x", "y"), v != 4)
    ) == jdict(x=3)


def test_key_select():
    assert jdict(x=3, y=4, z=5).key_select(lambda k: k in ("x", "y")) == jdict(x=3, y=4)


def test_value_select():
    assert jdict(x=3, y=4, z=5).value_select(lambda v: v != 4) == jdict(x=3, z=5)
