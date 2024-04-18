###
# filename: Queue.py
# purpose:  homework03 problem 1
# author:   Dr. Johnson
# date:     2023-02-21
###

import Node

class Queue:

   def __init__(self):
      self.front      = None
      self.queue_size = 0

   def insert(self,data):
      temp = Node(data)
      if self.front is None:
         self.front = temp
         self.queue_size =  self.queue_size + 1
      else:
         curr = self.front
         while curr.next != None:
            curr = curr.next
         curr.next = temp
         self.queue_size = self.queue_size + 1

   def remove(self):
      try:
         if self.front ==  None:
            print( "Sorry, Queue is Empty" )
         else:
            temp = self.front
            self.front = self.front.next
            tempdata = temp.data
            self.queue_size = self.queue_size-1
            del temp
            return tempdata
      except Exception as e:
         print(str(e))

   def isEmpty(self):
      return self.queue_size == 0

   def size(self):
      return self.queue_size

   def display(self):

q = Queue()
g.insert(23)
q.insert(29)
q.insert(17)
q.insert(11)
q.insert(31)
q.insert( 7)
q.insert(37)
