/*
 * File name: HuffmanCode.java
 * Purpose  : demonstrates use of building a tree to encode/decode a message using
 *             the Huffman Code scheme
 * @author  : B.J. Johnson
 * @date    : 2018-11-04
 * @version : 1.0.0
 *
 * Description:  Huffman coding is based on a histogram of the letters in a message.
 *                Each letter is counted and assigned a frequency.  The frequency
 *                values are used to insert the values as nodes in a priority queue.
 *                Then, starting from the lowest priority, the nodes are combined in
 *                such a way as to produce a binary tree in which each character is
 *                a single node in the tree.  To encode the message using the tree,
 *                you follow the path from the root to the letter which is in a leaf
 *                node; at each node if you take the left child you output a zero and
 *                if you take the right child you output a one.  The binary string
 *                thus built is guaranteed to have a unique binary sequence for each
 *                of the characters in the message.  This method is one way of encoding
 *                and decoding a message so that it takes less bits than transmitting
 *                Unicode or ASCII characters.
 *
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

class HuffmanCode {

   private static String message = "";
   private static char[] myCharArray = null;
   private static String[] codeArray = null;
   private static String codeString = "";
   private static String encodedMessage = "";

   private static BufferedReader input = new BufferedReader( new InputStreamReader( System.in ) );
   private static final int SIZE_OF_ALPHABET = 95;    // index @ zero with space as char - 32

  /**
   *  Constructor
   *     Just gets the message reading command line input until a blank line is read
   */
   public HuffmanCode() {
      String input;
      sayInstructions();
      BufferedReader br = new BufferedReader( new InputStreamReader( System.in ) );
      System.out.print( "\n\n\nEnter your message: " );
      try {
         input = br.readLine();
         while( input.length() != 0 ) {
            message = message + input;
            System.out.print( "Enter your continued message [empty line will quit entry]: " );
            input = br.readLine();
         }
      }
      catch( IOException ioe ) {};
      myCharArray = message.toCharArray();
      codeArray = new String[SIZE_OF_ALPHABET];
   }

  /**
   *  Method to output program instructions to the user
   */
   public void sayInstructions() {
      System.out.println( "\n\nThis program will perform Huffman encoding and decoding" +
                          "\n  on a string of text you enter.  The string will be turned" +
                          "\n  into a string of binary digits such that each character" +
                          "\n  in the input string has a unique binary pattern associated" +
                          "\n  with it in the output string." +
                          "\n\nWhen entering the string, pressing the [Enter] key when" +
                          "\n  the line is empty will cause the program to treat that as" +
                          "\n  the end of the message and begin processing." );
   }

  /**
   *  Method to display a prompt for the user to press 'ENTER' and wait for her to do so
   */
   public void pressEnter() {
      String inputLine = null;
      try {
         System.out.print( "      [Press 'ENTER' to continue]: >> " );
         inputLine = input.readLine();
      }
      catch( IOException ioe ) {
         System.out.println( "Caught IOException" );
      }
   }

  /**
   *  Method to display the contents of the ArrayList
   */
   public void printArrayList( ArrayList<HuffmanNode> table ) {
      for( int i = 0; i < table.size(); i++ ) {
         System.out.println( "  Huffman table[" + i + "]: " + table.get(i).toString() );
      }
   }

  /**
   *  Method to count the count of the characters in the message field
   *  @return int[] which contains the count of all letters in the message
   *  NOTE:  array is arranged in letter sorted order.  Range of characters is ASCII-based
   *           index is ASCII character value minus 32 so space is index zero
   */
   public int[] makeHistogram() {
      int[] histogram = new int[SIZE_OF_ALPHABET];
      for ( char c : myCharArray) {
         histogram[c - 32]++;
      }

      return histogram;
   }

  /**
   *  Method to make the Huffman table using HuffmanNodes
   *  @return ArrayList which contains HuffmanNode entries in sorted order
   *  NOTE:  array is arranged numeric order, lowest frequency to highest frequency; ties are resolved
   *           by sorting in character order.
   */
   public ArrayList makeHuffmanArray( int[] inputData ) {
      ArrayList<HuffmanNode> ht = new ArrayList<HuffmanNode>();
      for( int i = 0; i < SIZE_OF_ALPHABET; i++ ) {
         if( inputData[i] != 0 ) {
            HuffmanNode h = new HuffmanNode( (char)(i + 32), inputData[i], null, null );
            ht.add( h );
         }
      }
      Collections.sort( ht );
      return ht;
   }

  /**
   *  Method to recursively traverse the Huffman Tree
   *  @param node HuffmanNode which is root of [sub]tree we need to traverse
   */
   public void inOrderPrinter( HuffmanNode node ) {
      if( node.isLeaf() ) {
         System.out.print( node.toString() );
         return;
      }
      inOrderPrinter( node.getLeft() );
      System.out.print( node.toString() );
      inOrderPrinter( node.getRight() );
   }

  /**
   *  Method to make the Huffman tree using HuffmanNodes from the HuffmanNode table ArrayList
   *  @return a HuffmanNode which is the root node of the HuffmanTree structure
   *  NOTE:  array is arranged numeric order, lowest frequency to highest frequency; ties are resolved
   *           by sorting in character order.
   */
   public HuffmanNode makeHuffmanTree( ArrayList<HuffmanNode> nodeTable ) {
      int total = 0;
      HuffmanNode h = null;
      while( nodeTable.size() > 1 ) {
         total = nodeTable.get(0).getFrequency() + nodeTable.get(1).getFrequency();
         h = new HuffmanNode( ' ', total, null, null );
         h.setLeft( nodeTable.remove( 0 ) );
         h.setRight( nodeTable.remove( 0 ) );
         nodeTable.add( h );
         Collections.sort( nodeTable );
      }
      return nodeTable.get( 0 );
   }

  /**
   *  Method to make the Huffman code table for the letters in the message
   *  @param root HuffmanNode that is the root of the [sub]tree
   *  @param direction String that gets build up by recursion
   */
   public void makeEncodingTable( HuffmanNode root, String direction ) {
      if( root.isLeaf() ) {
         codeArray[root.getLetter() - 32] = direction.substring(1);
         codeString = "";
         return;
      } else {
         makeEncodingTable( root.getLeft(), direction + "0" );
         makeEncodingTable( root.getRight(), direction + "1" );
      }
   }


  /**
   *  Method to encode the original message as a string of ones and zeros
   *  @return a String object containing the ones and zeros for each character all smunched together
   */
   public String encodeMessage() {
      String output = "";
      for( int i = 0; i < message.length(); i++ ) {
         output += codeArray[message.charAt(i) - 32];
      }
      encodedMessage = output;
      return output;
   }

  /**
   *  Method to display characters of a message in terms of their ones and zeros at eight bits per
   */
   public void displayMessageAsCharacterBits() {
      String bitsForChars = "";
      for( int i = 0; i < message.length(); i++ ) {
         bitsForChars += Integer.toBinaryString( (int)message.charAt(i) );
      }
      System.out.println( "  actual message as bit string:" + bitsForChars + ":" );
   }

  /**
   *  Method to decode a bit stream into its corresponding message
   *  @param rootNode HuffmanNode that is the root of the encoded HuffmanTree structure
   */
   public void decodeMessage( HuffmanNode root ) {
      String output = "";
      int i = 0;
      HuffmanNode h = root;
      while( i < encodedMessage.length() ) {
         while( !(h.isLeaf()) ) {
            if( '0' == encodedMessage.charAt(i) ) {
               h = h.getLeft();
            } else if( '1' == encodedMessage.charAt(i) ) {
               h = h.getRight();
            }
            i++;
         }
         output += h.getLetter();
         h = root;
      }
      System.out.println( "\n  Decoded message is:\n    " + output );
   }

  /** ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   *  Main method to run the program
   *  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ */
   public static void main( String[] args ) {

     // the constructor asks the user for the message to be encoded
      HuffmanCode hc = new HuffmanCode();
      System.out.println( "\n  processing message: " + message );

     // make the histogram from the message, build the list of letter/frequency pairs
     //  and display the result
      int[] data = hc.makeHistogram();
      ArrayList table = hc.makeHuffmanArray( data );
      for( int i = 0; i < table.size(); i++ ) {
         System.out.println( "  Huffman table[" + i + "]: " + table.get(i).toString() );
      }

     // build the Huffman tree, then do an in-order traversal to display the result
      HuffmanNode treeRoot = hc.makeHuffmanTree( table );
      System.out.println( "\n  in-order tree traversal:" );
      hc.inOrderPrinter( treeRoot );
      System.out.println( "\n" );

     // traverse the tree again, using "0" for left and "1" for right
     //  to build up encoding strings and put them into the codeArray table
     //  then display that result
      hc.makeEncodingTable( treeRoot, "0" );
      System.out.println( "  values encoded from characters:" );
      for( String s : codeArray ) {
         if( s != null ) {
            System.out.print( s + " " );
         }
      }
      System.out.println( "\n" );

     // encode the message using the bits determined by the rest of this stuff
      System.out.println( "\n  encoded message is:" + hc.encodeMessage() + ":" );

     // for comparison, print out the entire message as its binary equivalent string
      hc.displayMessageAsCharacterBits();

     // now decode the message back to its original character form
      hc.decodeMessage( treeRoot );

      System.exit( 0 );
   }
}

