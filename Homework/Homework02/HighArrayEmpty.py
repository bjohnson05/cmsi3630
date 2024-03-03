###
# filename: HighArray.py
# purpose:  @see homework02 description at:
#    https://bjohnson.lmu.build/cmsi3530web/homework02.html
# author:   Dr. Johnson
# date:     2023-01-04
###

# global to the entire file
a = []         # empty list

# the class
class HighArray():

   # fields

   # initializer
   def __init__( self, maxSize ):
      a = []         # initialize the list to be empty [still]

   # find if a value is in the list
   def find( self, value ):
      for x in a:
         if( x == value ):
            return True
      return False

   # insert a value at the end of the list
   def insert( self, value ):
      a.append( value )
      return

   # delete a specific value
   def delete( self, value ):
      a.remove( value )
      return value

   # display
   def display( self ):
      return

   # get max goes here

   # noDupes goes here

# a little test to make sure the interpreter won't barf
h1 = HighArray( 10 )
h1.display()
