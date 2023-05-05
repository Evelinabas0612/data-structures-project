"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import pytest

from src.stack import Node, Stack


@pytest.fixture
def fixture_node():
    return Node(5, "data")


@pytest.fixture
def fixture_stack():
    stack = ['data1', 'data2', 'data3']
    return stack


def test_node(fixture_node):
    assert fixture_node.data == 5
    assert fixture_node.next_node == "data"
    assert type(fixture_node) == type(Node("qwer", "tyui"))


def test_stack(fixture_stack):
    assert fixture_stack == ['data1', 'data2', 'data3']
    assert len(fixture_stack) == 3


def test_push(fixture_node):
    stack = Stack()
    stack.push("top")
    stack.push("nexttop")
    node = stack.top
    assert isinstance(node, type(fixture_node))


def test__str__(fixture_stack):
    assert str(fixture_stack) == "['data1', 'data2', 'data3']"
