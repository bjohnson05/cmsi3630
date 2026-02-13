'''
   File:      IntList.py
   Purpose:   implements an integer sequential list
   @author:   Dr. Johnson
   date:      2026-01-24
   @version:  1.0.0
'''
class IntList:
   theList = [None]
   size = 0

   def __init__( self ):
      theList = list()
      size = 0;

   def checkIndex( self, index ):
      if( index > self.size ):
         return False
      return True

   def getValueAtIndex( self, index ):
      if( not self.checkIndex(index) ):
         return [None]
      else:
         return self.theList[index]

   def append( self, value ):
      if( self.size == 0 ):
         self.theList[0] = value
      else:
         self.theList.append( value )
      self.size += 1
      return

#   def insertValueAtIndex( self, index, value ):
#      return True

#   def prepend( self, value ):
#      return

   def removeValueAtIndex( self, index ):
      if( not self.checkIndex(index) ):
         return [None]
      else:
         return self.theList.pop( index )

   def printList( self ):
      print( "   List contents: ", self.theList )

def main():
   print( "\n\n   Python Integer List Tester" )
   print( "   ==========================" )
   print( "\n   Making new list:" );
   myList = IntList()
   myList.printList()
   myList.append( 23 )
   myList.append( 19 )
   myList.append( 29 )
   myList.append( 31 )
   myList.append( 41 )
   myList.append( 47 )
   print( "\n   Added six values to list: " )
   myList.printList()
   myList.append(  2 )
   myList.append(  3 )
   myList.append(  5 )
   myList.append(  7 )
   myList.append( 11 )
   myList.append( 13 )
   print( "\n   Added six more values to list: " )
   myList.printList()
   print( "\n   Removing value at index 7 from list: " )
   returnedValue = myList.removeValueAtIndex( 7 )
   print( "\n   Returned value: ", returnedValue )
   myList.printList()
   print( "\n   Getting value at index 7 from list: " )
   returnedValue = myList.getValueAtIndex( 7 )
   print( "\n   Returned value: ", returnedValue )
   myList.printList()
   print( "\n   Testing prepend() to front of list: " )
#   myList.prepend( 97 )
   myList.printList()
   print( "\n   Inserting value at index 7 into list: " )
#   returnedValue = myList.insertValueAtIndex( 7, 83 )
   myList.printList()

main()
