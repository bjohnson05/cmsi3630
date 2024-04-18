"""
filename: LinkedList.py
purpose:  demonstrate a linked list in python
author:   Dr. Johnson
date:     2023-01-06
"""

"""
This is the Node class for the list.
"""
class ListNode:

    # Constructor for the ListNode.
    def __init__(self, input = None): # default value!
        self.data = input
        self.next_node = None


"""
This is the linked list itself.
"""
class LinkedList:

    # constructor for the LinkedList.
    def __init__(self):
        self.head = None
        self.size = 0

    def __iter__(self):
        self.list_current = self.head
        return self

    def __next__(self):
        current_node = self.list_current
        self.list_current = self.list_current.next_node
        return current_node

    # Return the number of nodes in the list.
    def getSize(self):
        return self.size

    # Add a ListNode to the FRONT of the list.
    def prepend(self, dataToAdd):
        current_head = self.head
        self.head = ListNode(dataToAdd)
        self.head.next_node = current_head
        self.size += 1

    # Helper method to print the list.
    def print_list(self):
        current_node = self.head
        for i in range(self.size):
            print(current_node.data)
            current_node = current_node.next_node
