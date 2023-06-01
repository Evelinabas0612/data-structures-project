"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import pytest

from src.linked_list import Node, LinkedList


@pytest.fixture
def fixture_node():
    return Node()


@pytest.fixture
def fixture_linked_list():
    return LinkedList()


def test_node(fixture_node):
    assert fixture_node.data == None
    assert fixture_node.next_node == None


def test_linked_list(fixture_linked_list):
    fixture_linked_list.insert_beginning({'one': 1})
    fixture_linked_list.insert_at_end({'two': 2})
    assert str(fixture_linked_list) == "{'one': 1} -> {'two': 2} -> None"
    fixture_linked_list.insert_at_end({'three': 3})
    assert str(fixture_linked_list) == "{'one': 1} -> {'two': 2} -> {'three': 3} -> None"
    fixture_linked_list.insert_beginning({'zero': 0})
    assert str(fixture_linked_list) == "{'zero': 0} -> {'one': 1} -> {'two': 2} -> {'three': 3} -> None"


def test_to_list(fixture_linked_list):
    fixture_linked_list.insert_beginning({'id': 1, 'username': '11111'})
    fixture_linked_list.insert_at_end({'id': 2, 'username': '22222'})
    fixture_linked_list.insert_at_end({'id': 3, 'username': '33333'})
    fixture_linked_list.insert_at_end({'id': 4, 'username': '44444'})
    assert fixture_linked_list.to_list() == [{'id': 1, 'username': '11111'},
                                             {'id': 2, 'username': '22222'},
                                             {'id': 3, 'username': '33333'},
                                             {'id': 4, 'username': '44444'}]


def test_get_data_by_id(fixture_linked_list):
    fixture_linked_list.insert_beginning({'id': 1, 'username1': '11111'})
    fixture_linked_list.insert_beginning(45)
    fixture_linked_list.insert_at_end({'id': 4, 'username': '44444'})
    assert fixture_linked_list.get_data_by_id(1) == {'id': 1, 'username1': '11111'}
    assert fixture_linked_list.get_data_by_id(4) == {'id': 4, 'username': '44444'}
    assert fixture_linked_list.get_data_by_id(45) is None
    with pytest.raises(TypeError):
        fixture_linked_list.get_data_by_id(4 +'f')
