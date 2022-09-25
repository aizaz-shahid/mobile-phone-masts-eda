import pytest

from src.helpers import group_by_key, sort_data_by_key


@pytest.mark.parametrize("reverse", [True, False])
def test_sort_data_by_key(reverse):
    data = [{"id": i, "value": "some_value"} for i in range(5)]
    if reverse:
        expected = [{"id": i, "value": "some_value"} for i in reversed(range(5))]
    else:
        expected = [{"id": i, "value": "some_value"} for i in range(5)]
    sort_data_by_key(data=data, key="id", reverse=reverse)
    assert data == expected


def test_group_by_key():
    list_of_dicts = [
        {"key": "a", "value": 1},
        {"key": "a", "value": 2},
        {"key": "b", "value": 3},
    ]
    grouped_by_key = {"a": 2, "b": 1}
    assert group_by_key(list_of_dicts, key="key") == grouped_by_key
