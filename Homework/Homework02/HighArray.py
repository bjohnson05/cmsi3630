###
# filename: HighArray.py
# purpose:  @see homework02 description at:
#    https://bjohnson.lmu.build/cmsi3530web/homework02.html
# author:   Dr. Johnson
# date:     2023-01-04
###

# the class
class HighArray():

   # fields
   a = []

   # initializer
   def __init__( self ):
      a = []         # initialize the list to be empty [still]

   # find if a value is in the list
   def find( self, value ):
      for x in self.a:
         if( x == value ):
            return True
      return False

   # insert a value at the end of the list
   def insert( self, value ):
      self.a.append( value )
      return

   # delete a specific value
   def delete( self, value ):
      self.a.remove( value )
      return value

   # display
   def display( self ):
      print( self.a )
      return

   # get max
   def get_max( self ):
      x = self.a[0]
      for y in self.a:
         if( y > x ):
            x = y
      return x

   # remove duplicates
   def no_dupes( self ):
      b = []
      for x in self.a:
         if( x not in b ):
            b.append( x )
      self.a.clear()
      for x in b:
         self.a.append( x )
      return self.a

   def no_dupes2(self):
      self.a = list(set(self.a))
      return self.a
