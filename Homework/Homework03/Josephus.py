###
# filename: Josephus.py
# purpose:  demonstrates the Josephus puzzle
# author:   Dr. Johnson
# date:     2023-03-15
###

from CircularIntLinkedList import CircularIntLinkedList

DEBUG = False

def debugr( message ):
   if( DEBUG ):
      print( message )
   return

def press_enter():
   input( "   ...press 'enter'..." )
   return

class Josephus( CircularIntLinkedList ):

   def __init__( self ):
      self.my_list = CircularIntLinkedList()

   def do_step( self, count ):
      self.step()
      for i in range( count - 1 ):
         self.current = self.current.next
      self.remove( self.current.get_value() )
      return

def main():
   print( "\n\n   Josephus problem\n" )
   start_count = int( input( "   Enter the number of people in the circle: " ) )
   index = int( input( "   Now enter the number to count by: " ) )
   jo = Josephus()
   for i in range( start_count ):
      jo.insert( i )
   jo.step()
   jo.display()
   debugr( "   Ready to begin counting!" )
   while( jo.size > 1 ):
      jo.do_step( index )
      if( DEBUG ):
         jo.display()
      press_enter()
   print( "   Problem solved: " )
   print( "   with ", start_count, " people, counting by ", index )
   print( "   you should be number ", jo.current.get_value() )
   print( "\n" )
main()
