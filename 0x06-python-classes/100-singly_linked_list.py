#!/usr/bin/python3

"""_summary_

    Raises:
        TypeError: _description_
        TypeError: _description_

    Returns:
        _type_: _description_
"""


class Node:
    """
    This is a class representing a node
    """

    def __init__(self, data, next_node=None):
        """
        This is a node constructor

        Args:
            data (int): the value the node holds
            next_node (node, optional): pointer to the next node. Defaults to None.
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__data

    @data.setter
    def data(self, value):
        """_summary_

        Raises:
            TypeError: _description_
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node")
        self.__next_node = value


class SinglyLinkedList:
    """
    This is a class representing a singly linked list
    """

    def __init__(self, head=None):
        """
        This is a singly linked list constructor

        Args:
            head (node): the head of the linked list
        """

        self.__head = head

    def __str__(self):
        """
        This is a singly linked list string representation

        Returns:
            str: the string representation of the linked list
        """

        if self.__head is None:
            return "[]"

        current_node = self.__head
        string_representation = str(current_node.data)

        # while the next node is not none
        while current_node.next_node:
            if current_node.data < 0:
                string_representation += "\n"
            current_node = current_node.next_node
            string_representation += str(current_node.data) + "\n"
        return string_representation

    # def sorted_insert(self, value):
    #     """
    #     This is a singly linked list sorted insert

    #     Args:
    #         value (int): the value to insert
    #     """
    #     # If there is no value in the head or the list is empty
    #     if self.__head is None:
    #         self.__head = Node(value, self.__head)
    #         return
    def sorted_insert(self, value):
        """
        This is a singly linked list sorted insert

        Args:
            value (int): the value to insert
        """

        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node and value > current.next_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def get_head(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__head

    @staticmethod
    def counter(node):
        """
        This is a singly linked list counter

        Args:
            node (node): the node to count
        """

        count = 0
        while node:
            count += 1
            node = node.next_node
        return count
