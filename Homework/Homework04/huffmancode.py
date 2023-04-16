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
      self.codeList = []
      self.codeString = ""
      self.encodedMessage = ""
      self.SIZE_OF_ALPHABET = 95      # index @ zero with space as char - 32

      self.sayInstructions();
      self.inString = input( "\n\n\n   Enter your message: " );
      while( len( self.inString ) != 0 ):
         self.message = self.message + self.inString;
         self.inString = input( "Enter your continued message [empty line will quit entry]: " )
      self.myCharList = [*self.message]
      print( "   myCharList: ", self.myCharList )
#      codeArray = new String[SIZE_OF_ALPHABET];

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
  #  Method to display a prompt for the user to press 'ENTER'
  #   and wait for her to do so
  ###
   def pressEnter( self ):
      inputLine = ""
      print( "      [Press 'ENTER' to continue] ", end = "" )
      inputLine = input( " >> " )

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
      ht = []
      for i in range( self.SIZE_OF_ALPHABET ):
         if( inputData[i] != 0 ):
            h = HuffmanNode( (chr)(i + 32), inputData[i], None, None )
            ht.append( h )
      return ht

  ###
  #  Method to swap two nodes in a list
  ###
   def swapNodes( self, node1, node2 ):
      if( node1.compareTo( node2 ) < 0 ):
         temp = node1
         node1 = node2
         node2 = temp
      return node1, node2

  ###
  #  Method to sort the HuffmanNodes in the Huffman table
  #  NOTE:  array is arranged numeric order, lowest frequency to highest
  #         frequency; ties are resolved by sorting in character order.
  ###
   def sortHuffmanList( self, inputData ):
      for i in range( len( inputData ) ):
         for j in range( 0, len( inputData ) - i - 1 ):
            if( inputData[j] > inputData[j + 1] ):
               self.swapNodes( swapNodes[j], swapNodes[j + 1] )
      return inputData



hc = HuffmanCode()
hist = hc.makeHistogram()
huffmanTable = hc.makeHuffmanList( hist )
hc.printHuffmanTable( huffmanTable )
#huffmanTable = hc.sortHuffmanList( huffmanTable )
#hc.printHuffmanTable( huffmanTable )
