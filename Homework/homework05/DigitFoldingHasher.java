/**
 * filename: DigitFoldingHasher.java
 * purpose : Demonstrates hashing using a "digit folding" approach
 * @author : Dr. Johnson
 * @date   : 2018-11-23
 * @version: 1.0.0
 * Revision history: 2018-11-23 initial writing and release
 *
 * NOTE: Digit folding is a method of hashing which breaks the string of
 *       characters to be hashed into small chunks and adds them together.
 *       The chunk size is based [for base 10 numbers] on the number of
 *       zeros in the size of the array that is used for the Hash Table.
 *       See the description in the Lafore book on page 566 for details.
 */


/**
 * The DFH_DataItem class provides the data storage for each item,
 *  and also provides a public "getKey()" method to get its data
 *  since the data item is private to the class.
 */
class DFH_DataItem {

   private int    iData;         // integer data item (key)

  /**
   * constructor for integer data item
   * @param ii integer data for integer values
   */
   public DFH_DataItem( int ii ) {
      iData = ii;
   }

  /**
   * fetch the key for this DFH_DataItem since it's private
   * @return integer data for integer values
   */
   public int getKey() {
      return iData;
   }
}

public class DigitFoldingHasher {

   private static final int DIGIT_FOLD_MOD_VALUE   =  17;
   private static final int MAX_HASH_TABLE_SIZE    = 197;
   private static final int NON_ITEM               =  -1;
   private static final int GROUP_SIZE             =   3;

   private DFH_DataItem[]  hashArray;           // declare reference
   private int             arraySize = 197;     // just to start
   private int             currentCount;        // count of items

   public DigitFoldingHasher() {
      hashArray = new DFH_DataItem[arraySize];
      currentCount = 0;
   }

  /**
   * Method to hash an integer input using a "digit-folding" approach which
   *  splits the number into chunks, then hashes each chunk, adding up the
   *  results to get the key into the hash table.
   * @param d integer value to hash and provide the hash table index
   * @return integer index where to store the DFH_DataItem
   */
   public int hashFunction( int d ) {

     // if there are no more than 3 digits in the number, just hash the
     //  value and return the index; makes a shortcut.
      if( d <= 999 ) {
         return d % DIGIT_FOLD_MOD_VALUE;
      }

     // otherwise, do the chunky-monkey thing and mod by DIGIT_FOLD_MOD_VALUE
     //  to get the index; if there are extras, handle them before the mod
     //  operation
      boolean extra  = false;
      int groupCount = 0;
      int index      = 0;
      int j          = 0;
      int k          = 0;

      String sValue  = Integer.toString( d );
      int len = sValue.length();
      groupCount = len / GROUP_SIZE;
      if( (len % GROUP_SIZE) != 0 ) {
         groupCount++;
         j++;
         extra = true;
      }

      for( int i = 0; i < (groupCount - j) ; i++ ) {
         index += Integer.parseInt( sValue.substring( k, (k + 3) ) );
         k += 3;
      }
      if( extra ) {
         index += Integer.parseInt( sValue.substring( k, len ) );
      }
      return index % DIGIT_FOLD_MOD_VALUE;
   }

  /**
   * Method to insert a data item into the table
   *  @param item DFH_DataItem object to hash and insert in the HastTable
   *  NOTE: this is the original method from the Lafore book but with the
   *        input value changed to a DFH_DataItem instead of just DataItem
   *        to avoid confusion since all the files are in the same directory
   */
   public void insert( DFH_DataItem item ) {
      if( currentCount == arraySize ) {
         System.out.println( "   [Sorry, HashTable is full; delete something first.] " );
         return;
      }
      int key = item.getKey();               // extract key
      int hashVal = hashFunction( key );     // hash the key

      while( (hashArray[hashVal] != null) && (hashArray[hashVal].getKey() != -1) ) {
         ++hashVal;                          // go to next cell
         hashVal %= arraySize;               // wraparound if necessary
      }
      hashArray[hashVal] = item;
      currentCount++;
   }

  /**
   * Method to delete an integer data item from the table
   *  @param  key   integer value to search for and remove from the HastTable
   *  @return DFH_DataItem which was removed from the hash table
   *
   *  NOTE: this is the original method from the Lafore book but with the
   *        return value changed to a DFH_DataItem instead of just DataItem
   *        to avoid confusion since all the files are in the same directory
   */
   public DFH_DataItem delete( int key ) {
      int hashVal = hashFunction( key );              // hash the key

      while( hashArray[hashVal] != null ) {           // until empty cell,
         if( hashArray[hashVal].getKey() == key ) {
            DFH_DataItem temp  = hashArray[hashVal];  // save item
            hashArray[hashVal] = new DFH_DataItem( NON_ITEM );            // delete item
            currentCount--;
            return temp;                              // return item
         }
         ++hashVal;                                   // go to next cell
         hashVal %= arraySize;                        // wraparound if necessary
      }
      return null; // can’t find item
   }

  /**
   * Method to find a data item in the table
   *  @param  key   integer value to search for in the HastTable
   *  @return DFH_DataItem which was removed from the hash table
   *
   *  NOTE: this is the original method from the Lafore book but with the
   *        return value changed to a DFH_DataItem instead of just DataItem
   *        to avoid confusion since all the files are in the same directory
   */
   public DFH_DataItem find( int key ) {            // find item with key
      int hashVal = hashFunction( key );              // hash the key

      while( hashArray[hashVal] != null ) {     // until empty cell,
         if(hashArray[hashVal].getKey() == key) {
            return hashArray[hashVal];          // yes, return item
         }
         ++hashVal;                             // go to next cell
         hashVal %= arraySize;                  // wraparound if necessary
      }

      return null; // can’t find item
   }

  /**
   * Method to display the contents of the HashTable on the screen
   *  simply puts the number value or two stars for empty slots
   *  NOTE: slots that have been emptied contain a "-1" value and this
   *     routine replaces that with the stars for consistency
   */
   public void displayTable() {
      System.out.print( "\nTable: " );
      for( int j = 0; j < arraySize; j++ ) {
         if( (hashArray[j] != null) && (hashArray[j].getKey() != -1) ) {
            // System.out.print( hashArray[j].getKey() + " " );
            System.out.print( hashArray[j].getKey() + " " );
         } else {
            System.out.print( "** " );
         }
      }
      System.out.println("\n");
   }

}

