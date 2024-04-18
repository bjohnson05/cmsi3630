/**
 * filename: DigitFoldingHasherTester.java
 * purpose : Demonstrates hashing using a "digit folding" approach
 * @author : Dr. Johnson
 * @date   : 2018-11-25
 * @version: 1.0.0
 * Revision history: 2018-11-25 initial writing and release
 *
 * NOTE: Digit folding is a method of hashing which breaks the string of
 *       characters to be hashed into small chunks and adds them together.
 *       The chunk size is based [for base 10 numbers] on the number of
 *       zeros in the size of the array that is used for the Hash Table.
 *       See the description in the Lafore book on page 566 for details.
 */

import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;

public class DigitFoldingHasherTester {

   private DFH_DataItem[] HashTable;

  /**
   * Helper method to get a string from the user as input.
   *  @return String value the user has typed in
   */
   public static String getString() throws IOException {
      InputStreamReader isr = new InputStreamReader( System.in );
      BufferedReader    br  = new BufferedReader( isr );
      String s = br.readLine();
      return s;
   }

  /**
   * Helper method to get a char value from the user as input;
   *  calls the "getString()" method to handle the user input,
   *     and converts input to all lower-case for easy processing
   *  @return char value the user has typed in
   */
   public static char getFirstCharacter() throws IOException {
      String s = getString().toLowerCase();
      return s.charAt( 0 );
   }

  /**
   * Helper method to get an int value from the user as input;
   *  calls the "getString()" method to handle the user input.
   *  @return int value the user has typed in
   */
   public static int getInteger() throws IOException {
      String s = getString();
      return Integer.parseInt( s );
   }

  /**
   * Main method to run the program
   * @param args String array of the command line arguments
   */
   public static void main( String[] args ) {

      DigitFoldingHasher dfh = new DigitFoldingHasher();
      int aKey = 0;

      while( true ) {                     // basic Textual User Interface [TUI]
         System.out.print( "  Enter first letter of: " );
         System.out.print( "  [s]how, [i]nsert, [d]elete, [f]ind, or [q]uit: " );
         char choice = 'b';

         try {
            choice = getFirstCharacter();
         }
         catch( IOException ioe ) {};

         switch( choice ) {
            case 's':   System.out.print( "  Displaying: " );
                        dfh.displayTable();
                        break;
            case 'i':   System.out.print( "  Enter key value to insert: " );
                        try {
                           aKey = getInteger();
                        }
                        catch( IOException ioe ) {};
                        dfh.insert( new DFH_DataItem( aKey ) );
                        break;
            case 'd':   System.out.print( "  Enter key value to delete: " );
                        try {
                           aKey = getInteger();
                        }
                        catch( IOException ioe ) {};
                        dfh.delete( aKey );
                        break;
            case 'f':   System.out.print( "  Enter key value to find: " );
                        try {
                           aKey = getInteger();
                        }
                        catch( IOException ioe ) {};
                        DFH_DataItem di = dfh.find( aKey );
                        if( di == null ) {
                           System.out.println("    Could not find " + di.getKey() );
                        } else {
                           System.out.println("    Found " + di.getKey() );
                        }
                        break;
            case 'q':   System.out.print( "  Exiting program, thanks for playing!" );
                        System.exit( 0 );
            default:    System.out.print( "    [Sorry, invalid entry]\n" );
         }
      }
   }
}
