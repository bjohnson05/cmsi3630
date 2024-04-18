/**
 * filename: StringHashTable.java
 * purpose : Demonstrates a Hash Table with linear probing
 * @author : B.J. Johnson
 * @date   : 2018-11-23
 * @version: 1.0.0
 * Revision history: 2018-11-23: initial writing and release
 *
 * NOTE: This HashTable class uses Linear Probing to handle collisions
 *       when two values have the same hash.  The code is from the Lafore
 *       book, and is modified with a different hashing algorithm as in
 *       exercise 11.3, using a digit-folding approach.  The hash function
 *       has also been modified from the "index = (key) % arraySize" which
 *       assumes the key data is randomly distributed over its range.  As
 *       this is rarely the case, a different algorithm that handles String
 *       input has been substituted instead.
 */

/**
 * The DataItem class provides the data storage for each item,
 *  and also provides a public "getKey()" method to get its data
 *  since the data item is private to the class.
 */
class DataItem {

   private int    iData;         // integer data item (key)
   private String sData;         // String data item (key) added for homework solution

  /**
   * constructor for integer data item
   * @param ii integer data for integer values
   */
   public DataItem( int ii ) {
      iData = ii;
   }

  /**
   * constructor for String data item; added for homework solution
   * @param ss String data for String values
   */
   public DataItem( String ss ) {
      sData = ss;
   }

  /**
   * fetch the key for this DataItem since it's private
   * @return integer data for integer values
   */
   public int getKey() {
      return iData;
   }

  /**
   * fetch the int key for this DataItem since it's private
   *  copy to differentiate for homework solution
   * @return ss String data for String values
   */
   public int getIntKey() {
      return iData;
   }

  /**
   * fetch the String key for this DataItem since it's private
   *  added to differentiate for homework solution
   * @return ss String data for String values
   */
   public String getStringKey() {
      return sData;
   }
}

/**
 * Here is the HashTable class.
 */
class HashTable {

   private DataItem[] hashArray;    // array holds hash table
   private int arraySize;           // size of the array; should be a prime number
   private DataItem nonItem;        // for deleted items
   private int currentCount;        // how many items we have

   private static final int modFactor = 37;

  /**
   * Constructor
   */
   public HashTable( int size ) {
      arraySize    = size;
      hashArray    = new DataItem[arraySize];
      nonItem      = new DataItem( -1 ); // deleted item key is -1
      currentCount = 0;
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
            System.out.print( hashArray[j].getStringKey() + " " );
         } else {
            System.out.print( "** " );
         }
      }
      System.out.println("\n");
   }

  /**
   * Method to Hash the input.  This is the original one which handles int's
   *  @param key int value to hash for installing in the table
   *  @return hands back the index value to the table that is the hash result
   */
   public int hashFunc( int key ) {
      System.out.println( "    [Hash of " + key + " is: " + (key % arraySize) + "]" );
      return key % arraySize;
   }

  /**
   * Method to Hash the input.  This one takes a String as input.
   *  @param key String value to hash for installing in the table
   *  @return hands back the index value to the table that is the hash result
   */
   public int hashFunc( String key ) {
      key = key.toLowerCase();
      int maxCount = key.length() - 1;
      int index    = 0;
      double j     = 0.0;
      for( int i = maxCount; i >=0; i-- ) {
         int c = (key.codePointAt(i) - 32);
         index += (c * Math.pow( 27.0, j )) % modFactor;
         j = j + 1.0;
      }
      return index;
   }

  /**
   * Method to insert a data item into the table
   *  @param  item   DataItem object to hash and insert in the HastTable
   */
   public void insert( DataItem item ) {
      if( currentCount == arraySize ) {
         System.out.println( "   [Sorry, HashTable is full; delete something first.] " );
         return;
      }
      // int key = item.getKey();               // extract key
      String key = item.getStringKey();      // extract key [replaces integer version for homework]
      int hashVal = hashFunc( key );         // hash the key

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
   *  NOTE: this is the original method from the Lafore book
   */
   public DataItem delete( int key ) {
      int hashVal = hashFunc( key );            // hash the key

      while( hashArray[hashVal] != null ) {     // until empty cell,
         if( hashArray[hashVal].getKey() == key ) {
            DataItem temp = hashArray[hashVal]; // save item
            hashArray[hashVal] = nonItem;       // delete item
            currentCount--;
            return temp;                        // return item
         }
         ++hashVal;                             // go to next cell
         hashVal %= arraySize;                  // wraparound if necessary
      }
      currentCount--;
      return null; // can’t find item
   }

  /**
   * Method to delete a data item from the table
   *  @param  key String value to search for and remove from the HastTable
   *  NOTE: added to handle String key for homework
   */
   public DataItem delete( String key ) {
      int hashVal = hashFunc( key );            // hash the key

      while( hashArray[hashVal] != null ) {     // until empty cell,
         // if( hashArray[hashVal].getKey() == key ) {
         if( hashArray[hashVal].getStringKey().equals( key ) ) {
            DataItem temp = hashArray[hashVal]; // save item
            hashArray[hashVal] = nonItem;       // delete item
            currentCount--;
            return temp;                        // return item
         }
         ++hashVal;                             // go to next cell
         hashVal %= arraySize;                  // wraparound if necessary
      }
      currentCount--;
      return null; // can’t find item
   }

  /**
   * Method to find a data item in the table
   *  @param  key   integer value to search for in the HastTable
   *  NOTE: this is the original method from the Lafore book
   */
   public DataItem find( int key ) {            // find item with key
      int hashVal = hashFunc( key );              // hash the key

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
   * Method to find a data item in the table
   *  @param  key String value to search for in the HastTable
   *  NOTE: added to handle String key for homework
   */
   public DataItem find( String key ) {            // find item with key
      int hashVal = hashFunc( key );              // hash the key

      while( hashArray[hashVal] != null ) {     // until empty cell,
         // if(hashArray[hashVal].getKey() == key) {
         if(hashArray[hashVal].getStringKey().equals( key )) {
            return hashArray[hashVal];          // yes, return item
         }
         ++hashVal;                             // go to next cell
         hashVal %= arraySize;                  // wraparound if necessary
      }

      return null; // can’t find item
   }

} // end class HashTable
