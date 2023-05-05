"""Здесь надо написать тесты с использованием unittest для модуля queue."""

import pytest

from src.queue import Node, Queue


@pytest.fixture
def fixture_node():
    return Node(5, "data")


@pytest.fixture
def fixture_queue():
    queue = Queue()
    return queue


def test_node(fixture_node):
    assert fixture_node.data == 5
    assert fixture_node.next_node == "data"
    assert type(fixture_node) == type(Node("qwer", "tyui"))


def test_queue(fixture_queue):
    assert fixture_queue.head == None
    assert fixture_queue.tail == None
    assert type(fixture_queue) == type(Queue())


def test_enqueue(fixture_queue):
    fixture_queue.enqueue("head")
    assert fixture_queue.head.data == "head"
    assert fixture_queue.tail.data == "head"
    fixture_queue.enqueue("tail")
    assert fixture_queue.head.data == "head"
    assert fixture_queue.tail.data == "tail"


