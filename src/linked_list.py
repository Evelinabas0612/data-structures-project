class Node:
    """Класс для узла односвязного списка"""
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        self.head = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            node.next_node = self.head
            self.head = node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        node = Node(data)

        if not self.head:
            self.head = node
            return
        tail = self.head
        while tail.next_node:
            tail = tail.next_node
        tail.next_node = node

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string.strip()

    def to_list(self) -> list:
        """Возвращает список с данными, содержащимися в односвязном списке LinkedList"""

        result_list = []
        current_node = self.head

        while current_node:
            result_list.append(current_node.data)
            current_node = current_node.next_node
        return result_list

    def get_data_by_id(self, id_value: int) -> dict:
        """Возвращает первый найденный в LinkedList словарь с ключом 'id',
           значение которого равно переданному в метод значению"""
        current_node = self.head
        while current_node:
            try:
                if current_node.data['id'] == id_value:
                    return current_node.data

            except TypeError:
                print("Неподходящий формат данных")
            current_node = current_node.next_node






