###
# filename: DequeApp.py
# purpose:  demonstration of a deque for homework03
# author:   Dr. Johnson
# date:     2023-03-13
###

from Deque import Deque

def main():

   d = Deque( 8 )
   print( "   Inserting four from the left and four from the right." )
   d.insert_left( 2 )
   d.insert_left( 3 )
   d.status()
   d.insert_right( 11 )
   d.insert_right( 13 )
   d.status()
   d.insert_left( 5 )
   d.insert_left( 7 )
   d.insert_right( 17 )
   d.insert_right( 19 )
   d.status()
   print( "   Attempting one more insert from each end." )
   d.insert_right( 23 )
   d.insert_left( 23 )
   d.display()
   print( "   removing from left, got:", d.remove_left() )
   print( "   removing from left, got:", d.remove_left() )
   print( "   removing from left, got:", d.remove_left() )
   print( "   removing from left, got:", d.remove_left() )
   d.status()
   print( "   removing from right, got:", d.remove_right() )
   print( "   removing from right, got:", d.remove_right() )
   print( "   removing from right, got:", d.remove_right() )
   print( "   removing from right, got:", d.remove_right() )
   d.status()
   print( "   removing from left, got:", d.remove_left() )
   print( "   removing from right, got:", d.remove_right() )

   print( "   Filling up Deque again for wrap-around display test" )
   d.insert_left( 22 )
   d.insert_left( 23 )
   d.insert_left( 25 )
   d.insert_left( 27 )
   d.insert_right( 31 )
   d.insert_right( 33 )
   d.insert_right( 37 )
   d.insert_right( 39 )
   d.status()
   d.display()
   print( "   Removing a couple from left and right end" )
   d.remove_left()
   d.remove_left()
   d.remove_right()
   d.status()
   d.display()
main()
