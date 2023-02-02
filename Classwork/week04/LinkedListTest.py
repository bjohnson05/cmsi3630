"""
filename: LinkedListTest.py
purpose:  test the LinkedList demonstrator
author:   Dr. Johnson
date:     2023-01-08
"""

import LinkedList

my_list = LinkedList.LinkedList()

my_list.prepend(23)
my_list.prepend(19)
my_list.prepend(17)
my_list.prepend(13)
my_list.prepend(11)
my_list.prepend(7)
my_list.prepend(5)
my_list.prepend(3)
my_list.prepend(2)
print(f"\nList now has size:{my_list.getSize()}")
my_list.print_list()

it = iter(my_list)
print(f"\nCurrent node is:{next(it).data}")
print(f"Current node is:{next(it).data}")
print(f"Current node is:{next(it).data}")
print(f"Current node is:{next(it).data}")
print(f"Current node is:{next(it).data}")
print(f"Current node is:{next(it).data}")
print(f"Current node is:{next(it).data}")
print(f"Current node is:{next(it).data}")
print(f"Current node is:{next(it).data}")
