/**
 * filename: StringHashTableTester.java
 * purpose : Demonstrates a Hash Table with linear probing
 * @author : B.J. Johnson
 * @date   : 2018-11-23
 * @version: 1.0.0
 * @version: 2.0.0
 * Revision history: 2018-11-23: initial writing and release
 *                   2018-11-25: updated to perform String hashing
 */

import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;

class StringHashTableTester {

   public static void main( String[] args ) throws IOException {
      DataItem aDataItem;

      int aKey, size, n, keysPerCell;

     // added the following to change to string handling for homework
      String sKey;
      String[] initData = { "Now", "is", "the", "time", "for", "all", "good", "men",
                            "and", "women", "to", "come", "to", "the", "aid", "of",
                            "their", "country" };

      System.out.print( "\n  Enter size of hash table: " );
      size = getInt();
     // Commented out from integer version to enable String hashing for homework
     // System.out.print( "  Enter initial number of items: " );
     // n = getInt();
      n = initData.length;
      keysPerCell = 10;
      HashTable theHashTable = new HashTable( size );

     // insert initial data
      for( int j = 0; j < n; j++ ) {
        // aKey = (int)(java.lang.Math.random() * keysPerCell * size);
        // aDataItem = new DataItem( aKey );
         sKey = initData[j];
         aDataItem = new DataItem( sKey );
         theHashTable.insert( aDataItem );
      }

     // interact with user; basic TUI using first letter of input
      while( true ) {
         System.out.print( "  Enter first letter of: " );
         System.out.print( "  [s]how, [i]nsert, [d]elete, [f]ind, or [q]uit: " );
         char choice = getChar();

         switch( choice ) {
            case 's':   theHashTable.displayTable();
                        break;
            case 'i':   System.out.print( "  Enter key value to insert: " );
                        // aKey = getInt();
                        // aDataItem = new DataItem( aKey );
                        aDataItem = new DataItem( getString() );
                        theHashTable.insert( aDataItem );
                        break;
            case 'd':   System.out.print( "  Enter key value to delete: " );
                        // aKey = getInt();
                        // theHashTable.delete( aKey );
                        theHashTable.delete( getString() );
                        break;
            case 'f':   System.out.print( "  Enter key value to find: " );
                        // aKey = getInt();
                        // aDataItem = theHashTable.find( aKey );
                        aDataItem = theHashTable.find( getString() );
                        if( aDataItem != null ) {
                           // System.out.println("    Found " + aKey );
                           System.out.println("    Found " + aDataItem.getStringKey() );
                        } else {
                           // System.out.println("    Could not find " + aKey );
                           System.out.println("    Could not find " + aDataItem.getStringKey() );
                        }
                        break;
            case 'q':   System.out.print( "  Exiting program, thanks for playing!" );
                        System.exit( 0 );
            default:    System.out.print( "    [Sorry, invalid entry]\n" );
         }
      }
   }

  /**
   * Helper method to get a string from the user as input.
   *  @return String value the user has typed in
   */
   public static String getString() throws IOException {
      InputStreamReader isr = new InputStreamReader( System.in );
      BufferedReader br = new BufferedReader( isr );
      String s = br.readLine();
      return s;
   }

  /**
   * Helper method to get a char value from the user as input;
   *  calls the "getString()" method to handle the user input,
   *     and converts input to all lower-case for easy processing
   *  @return char value the user has typed in
   */
   public static char getChar() throws IOException {
      String s = getString().toLowerCase();
      return s.charAt( 0 );
   }

  /**
   * Helper method to get an int value from the user as input;
   *  calls the "getString()" method to handle the user input.
   *  @return int value the user has typed in
   */
   public static int getInt() throws IOException {
      String s = getString();
      return Integer.parseInt( s );
   }

}
