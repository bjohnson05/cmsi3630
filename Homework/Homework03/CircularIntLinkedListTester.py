###
# filename: CircularIntLinkedListTester.py
# purpose:  demonstrator for circular linked list
# author:   Dr. Johnson
# date:     2023-03-14  HAPPY PI DAY!
###

from CircularIntLinkedList import CircularIntLinkedList

class CircularIntLinkedListTester:

   def __init__( self ):
      my_list = None

def main():
   print( "\n   Welcome to the Circular Linked List Test App\n" )

   cll = CircularIntLinkedList()
   cll.display()
   cll.insert( 23 )
   cll.insert( 29 )
   cll.insert( 31 )
   cll.insert( 37 )
   cll.display()
   print( "   Searching for 23: ", cll.search( 23 ) )
   print( "   Searching for 42: ", cll.search( 42 ) )
   print( "   Removing node 23: value is: ", cll.remove( 23 ) )
   cll.display()
   cll.insert( 333 )
   cll.insert( 222 )
   cll.insert( 111 )
   cll.insert( 99 )
   cll.insert( 88 )
   cll.insert( 77 )
   cll.insert( 66 )
   cll.insert( 55 )
   cll.insert( 44 )
   cll.insert( 33 )
   cll.insert( 22 )
   cll.insert( 11 )
   cll.display()
   print( "   Removing node 111: value is: ", cll.remove( 111 ) )
   print( "   Removing node  55: value is: ", cll.remove( 55 ) )
   print( "   Removing node  88: value is: ", cll.remove( 88 ) )
   cll.display()
   print( "   Testing step() method, list display should start with 77..." )
   cll.step()
   cll.display()
   print( "   Testing step() method 3X, list display should start with 33...." )
   cll.step()
   cll.step()
   cll.step()
   cll.display()

main()

