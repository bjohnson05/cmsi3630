###
# filename: huffmannode.py
# purpose: implement a node for the Huffman coding problem
# author: Dr. Johnson
# date: 2023-04-11
###

class HuffmanNode:

  # constructor
   def __init__( self, letter, count, leftChild, rightChild ):
      self.myChar = letter
      self.frequency = count
      self.left = leftChild
      self.right = rightChild
      self.code = ""

  # method to return the letter in the node
   def getLetter( self ):
      return self.myChar

  # method to set the left child node
   def setLeft( self, node ):
      self.left = node
      return

  # method to set the right child node
   def setRight( self, node ):
      self.right = node
      return

  # method to get the left child node
   def getLeft( self ):
      return self.left

  # method to get the right child node
   def getRight( self ):
      return self.right

  # method to determine if this node is a leaf
   def isLeaf( self ):
      return self.left == None and self.right == None

  # method to return a string version of this node
  #   outputs a node representation like "[ A | 3 ]"
   def toString( self ):
      output = "[" + self.myChar + "|" + str(self.frequency) + "|" + self.code + "]"
      return output

  # method to set the code string value of the node
   def setCodeString( self, value ):
      self.code = value

  # method to get the code string value of the node
   def getCodeString( self ):
      return self.code

  # method to compare another node to this node
  #   note that this compares frequency first ~
  #   if not equal returns the difference between this and other
  #   if frequency values are equal ~
  #      returns difference between characters using 'ord()'
  #   example: this => '[ a | 1 ]' and other => '[ h | 1 ]'
  #      frequency is tied, returns 97 - 104 = -7
  #      NEGATIVE value means other comes later
   def compareTo( self, other ):
      if not self.frequency == other.frequency:
         return self.frequency - other.frequency
      else:
         return ord(self.myChar) - ord(other.myChar)

###
#  Test area to check out all the Huffman Node methods;
###
print( "\n\n   Running Huffman Node tests." )
print( "   ===========================" )
print( "   Creating Huffman Nodes 'A', 'B', and 'C'..." )
print( "     Frequency values are '1', '2', and '1'..." )
hn1 = HuffmanNode( "A", 1, None, None )
hn2 = HuffmanNode( "B", 2, None, None )
hn3 = HuffmanNode( "C", 1, None, None )

print( "   Testing toString() method..." )
print( hn1.toString() )
print( hn2.toString() )
print( hn3.toString() )

print( "   Testing compareTo() method on hn2 to hn3..." )
print( "      expecting +1 and got: ", hn2.compareTo( hn3 ) )
print( "   Testing compareTo() method on hn1 to hn3..." )
print( "      expecting -2 and got: ", hn1.compareTo( hn3 ) )

print( "   Creating Huffman Node 'H'...." )
hn4 = HuffmanNode( "H", 1, None, None )
print( hn4.toString() )

print( "   Testing compareTo() method on hn1 to hn4..." )
print( "      expecting -7 and got: ", hn1.compareTo( hn4 ) )

print( "   Testing 'isLeaf()' method on hn1 with no children..." )
print( "      expecting True and got: ", hn1.isLeaf() )

print( "   Testing setLeft() and setRight() methods to hn1..." )
print( "      setLeft( hn2 ) and setRight( hn3 )...." )
hn1.setLeft( hn2 )
hn1.setRight( hn3 )

print( "   Testing getLeft() and getRight() methods to hn1..." )
print( "    expecting left of '[B|2|]' and got: ", hn1.getLeft().toString() )
print( "    expecting right of '[C|1|]' and got: ", hn1.getRight().toString() )

print( "   Testing 'isLeaf()' method on hn1 with two children..." )
print( "      expecting True and got: ", hn1.isLeaf() )

print( "   Testing 'getLetter()' method on hn1, then hn1's left child..." )
print( "      expecting 'A' then 'B' and got: ", hn1.getLetter(), " and: ", hn1.getLeft().getLetter() )

print( "   Testing set and get code string method on hn1..." )
print( "      setting code to '110'..." )
hn1.setCodeString( "110" )
print( "      expecting '110' and got: ", hn1.getCodeString() )

print( "   Testing toString() method again for hn1..." )
print( "      expecting '{A|1|110]' and got: ", hn1.toString() )

print( "\n\n   End of Huffman Node tests." )
print( "   ==========================" )
