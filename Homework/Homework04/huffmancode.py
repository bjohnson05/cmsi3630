###
# filename: huffmancode.py
# purpose: demonstrates use of building a tree to encode/decode
#            a message using the Huffman Code scheme
# author:   Dr. Johnson
# date:     2023-04-14
###

from huffmannode import HuffmanNode

class HuffmanCode:

  ###
  #  Constructor
  #     initializes variables, then gets the message, reading command line input
  #     until a blank line is read
  ###
   def __init__( self ):
      self.message = ""
      self.myCharList = []
      self.codeTable = []
      self.codeString = ""
      self.encoding = ""
      self.SIZE_OF_ALPHABET = 95      # index @ zero with space as char - 32

      self.sayInstructions();
      self.inString = input( "\n\n\n   Enter your message: " );
      while( len( self.inString ) != 0 ):
         self.message = self.message + self.inString;
         self.inString = input( "Enter your continued message [empty line will quit entry]: " )
      self.myCharList = [*self.message]
      print( "\n   myCharList: ", self.myCharList )

  ###
  #  Method to output program instructions to the user
  ###
   def sayInstructions( self ):
      print( "\n\n   This program will perform Huffman encoding and decoding" )
      print( "   on a string of text you enter.  The string will be turned" )
      print( "   into a string of binary digits such that each character" )
      print( "   in the input string has a unique binary pattern associated" )
      print( "   with it in the output string." )
      print( "\n   When entering the string, pressing the [Enter] key when" )
      print( "   the line is empty will cause the program to treat that as" )
      print( "   the end of the message and begin processing." )

  ###
  #  Method to display the contents of the Huffman 'table'
  ###
   def printHuffmanTable( self, table ):
      print( "      in printHuffmanTable(), size of table: ", len( table ) )
      for i in range( len( table ) ):
         print( "  Huffman table[", i, "]: ", table[i].toString() )

  ###
  #  Method to count the counts of the characters in the message
  #  NOTE:  array is arranged in letter sorted order.
  #         Range of characters is ASCII-based
  #         index is ASCII character value minus 32 so space is index zero
  ###
   def makeHistogram( self ):
      print( "\n   Making the histogram of the message letters..." )
      histogram = [0] * self.SIZE_OF_ALPHABET
      for c in self.myCharList:
         histogram[ord(c) - 32] += 1
      return histogram

  ###
  #  Method to make the Huffman table using HuffmanNodes
  #  NOTE:  array is arranged numeric order by their ASCII character values
  #         as indices, and will need to be sorted
  ###
   def makeHuffmanList( self, inputData ):
      print( "\n   Making the list from the input histogram..." )
      ht = []
      for i in range( self.SIZE_OF_ALPHABET ):
         if( inputData[i] != 0 ):
            h = HuffmanNode( (chr)(i + 32), inputData[i], None, None )
            ht.append( h )
      return ht

  ###
  #  Method to compare two Huffman nodes 'table'
  #   if node1 number value > node2 number value then return positive
  #   if node1 number value < node2 number value then return negative or zero
  #   if
  ###
   def compareTo( self, node1, node2 ):
      if( node1.frequency > node2.frequency ):
         return node1.frequency - node2.frequency
      elif( node1.frequency == node2.frequency ):
         if( node1.myChar < node2.myChar ):
            return ord( node1.myChar ) - ord( node2.myChar )
         else:
            return ord( node2.myChar ) - ord( node1.myChar )
      else:
         return node1.frequency - node2.frequency


  ###
  #  Method to sort the HuffmanNodes in the Huffman table
  #  NOTE:  array is arranged numeric order, lowest frequency to highest
  #         frequency; ties are resolved by sorting in character order.
  ###
   def sortHuffmanList( self, inputData ):
      print( "   Sorting the list of Huffman Nodes..." )
      for i in range( len( inputData ) ):
         for j in range( 0, len( inputData ) - i - 1 ):
            if( self.compareTo( inputData[j], inputData[j + 1] ) > 0 ):
               inputData[j + 1], inputData[j] = inputData[j], inputData[j + 1]
      return inputData

  ###
  #  Method to use the Huffman Table to create the Huffman Tree
  ###
   def createHuffmanTree( self, inputData ):
      print( "\n   Creating Huffman Tree..." )
      while( len( inputData ) > 1 ):
         freq = inputData[0].frequency + inputData[1].frequency
         node = HuffmanNode( '?', freq, inputData[0], inputData[1] )
         if( len(inputData) > 1 ):
            inputData.pop( 0 )
            inputData[0] = node
         else:
            inputData[0] = node
         self.sortHuffmanList( inputData )
      return inputData

  ###
  #  Method to traverse the Huffman Tree to display for verification
  ###
   def inOrderTraversal( self, currentNode ):
      if( currentNode.isLeaf() ):
         print( currentNode.toString(), end = "" )
         return
      else:
         self.inOrderTraversal( currentNode.getLeft() )
         print( currentNode.toString(), end = "" )
         self.inOrderTraversal( currentNode.getRight() )

  ###
  #  Method to use the Huffman Tree to build the encoded output
  #      based on the inOrderTraversal above
  ###
   def encode( self, currentNode, searchLetter ):
      if( currentNode.isLeaf() ):
         if( currentNode.getLetter() == searchLetter):
            currentNode.code = self.codeString
            self.encoding += self.codeString
         return
      else:
         self.codeString += '0'
         self.encode( currentNode.getLeft(), searchLetter )
         self.codeString = self.codeString[:-1]
         self.codeString += '1'
         self.encode( currentNode.getRight(), searchLetter )
         self.codeString = self.codeString[:-1]

###
#  Method to use the encoded input of ones and zeros to work\
#     through the tree and get the letters back for the message
###
   def decode( self, root, encodedString ):
      output = ""
      temp = root
      i = 0
      while( i < len( encodedString ) ):
         if( temp.getLetter() == '?' ):
            if( encodedString[i] == '0' ):
               temp = temp.getLeft()
            elif( encodedString[i] == '1' ):
               temp = temp.getRight()
            i += 1
         else:
            output += temp.myChar
            temp = root
      output += temp.getLetter()
      return output

###
# program to make the huffman code for the message that the user typed
#  step 1: make a histogram of the total count of each letter in the message
#  step 2: put the nodes from step one into a list
#  step 3: sort the list in ascending order by letter frequency
#           if there's a tie, sort ascending by letter value
#  step 4: build a tree using the Huffman tree-building scheme
#  step 5: build an encoding table of the binary equivalent for each
#           letter in the message by traversing the tree, using the
#           Huffman encoding of "0" for left and "1" for right
#  step 6: use the table from step 5 to encode the message
###
hc = HuffmanCode()

# step 1
hist = hc.makeHistogram()

# step 2
huffmanTable = hc.makeHuffmanList( hist )
hc.printHuffmanTable( huffmanTable )

# step 3
huffmanTable = hc.sortHuffmanList( huffmanTable )
hc.printHuffmanTable( huffmanTable )

# step 4
huffmanTable = hc.createHuffmanTree( huffmanTable )
print( "\n   Huffman Tree created, traversing for proof..." )
hc.inOrderTraversal( huffmanTable[0] )

# step 5
print( "\n\n   building encoding table using Huffman Tree..." )
i = 0
while( i < len( hc.message ) ):
   hc.codeString = ''
   hc.encode( huffmanTable[0], hc.message[i] )
   i += 1
print( "\n   Huffman Tree updated, traversing for proof..." )
hc.inOrderTraversal( huffmanTable[0] )

# step 6
print( "\n\n   Encoded message is: ", hc.encoding )

# now feed the encoding string back through the tree to
#  decode the message
hc.message = hc.decode( huffmanTable[0], hc.encoding )
print( "\n\n   Decoded message is: ", hc.message )

