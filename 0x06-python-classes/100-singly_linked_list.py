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
            next_node (node, optional): pointer to the next node.
            Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter for the data

        Returns:
            _int_: the data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter for the data

        Raises:
            TypeError: if the value isnt a number
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Getter for next_node property

        Returns:
            _Node_: next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter function for the next node

        Args:
            value (_int_): number value

        Raises:
            TypeError: if value or Node is not of the same type
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
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
# if the list is empty is i return an empty string
        if self.__head is None:
            return ""

        current_node = self.__head
        string_representation = ""

        # while the next node is not none
        while current_node:
            string_representation += str(current_node.data) + "\n"
            current_node = current_node.next_node
        return string_representation[:-1]

    def sorted_insert(self, value):
        """
        This is a singly linked list sorted insert

        Args:
            value (int): the value to insert
        """

        new_node = Node(value)
        current = self.__head
        if current is None:
            self.__head = new_node
            return
        if value < current.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while current.next_node and value > current.next_node.data:
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node

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

    def get_head(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__head
