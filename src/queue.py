class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node

    def __str__(self):
        if self.next_node:
            return f"{self.data}\n{self.next_node}"
        return f"{self.data}"

class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        if self.tail:
            self.tail.next_node = Node(data, self.tail.next_node)
            self.tail = self.tail.next_node
        else:
            self.head = self.tail = Node(data, None)

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if self.head is not None:
            return_data = self.head.data
            self.head = self.head.next_node
            return return_data
        else:
            return None

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        if self.head:
            return f"{self.head}"
        else:
            return f""
