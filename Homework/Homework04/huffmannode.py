###
# filename: huffmannode.py
# purpose: implement a node for the Huffman coding problem
# author: Dr. Johnson
# date: 2023-04-11
###

class HuffmanNode:

   def __init__( self, letter, count, leftChild, rightChild ):
      self.myChar = letter
      self.frequency = count
      self.left = leftChild
      self.right = rightChild
#      print( "[", self.myChar, "|", self.frequency, "]" )

   def getLetter( self ):
      return self.myChar

   def setLeft( self, node ):
      self.leftChild = node
      return

   def setRight( self, node ):
      self.rightChild = node
      return

   def getLeft( self ):
      return self.left

   def getRight( self ):
      return self.right

   def isLeaf( self ):
      return self.left == None and self.right == None

   def toString( self ):
      output = "[" + self.myChar + "|" + str(self.frequency) + "]"
      return output

   def compareTo( self, other ):
      if not self.frequency == other.frequency:
         return self.frequency - other.frequency
      else:
         return ord(self.myChar) - ord(other.myChar)

# test code
hn1 = HuffmanNode( "A", 1, None, None )
print( hn1.toString() )
hn2 = HuffmanNode( "B", 2, None, None )
hn3 = HuffmanNode( "C", 1, None, None )
print( hn2.toString() )
print( hn3.toString() )
print( hn2.compareTo( hn3 ) )
print( hn1.compareTo( hn3 ) )
