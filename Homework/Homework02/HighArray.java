/* ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 *  HighArray.java
 *  Array demonstration class
 * ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ */
import java.util.Set;
import java.util.HashSet;

class HighArray {

   private long[] a;       // ref to array a
   private int nElems;     // number of data items

  /**
   * Constructor
   */
   public HighArray( int max ) {
      a = new long[max]; // create the array
      nElems = 0; // no items yet
   }

  /**
   * Method to find a value in the array
   */
   public boolean find( long searchKey ) {
      int j;
      for( j = 0; j < nElems; j++ ) {
         if( a[j] == searchKey ) {
            break;
         }
      }
      if( j == nElems ) {
         return false; // yes, can’t find it
      } else {
         return true; // no, found it
      }
   }

  /**
   * Method to insert a value at the end of the array
   *  NOTE: this should actually be called "append()" but this is
   *        code directly from the text book
   */
   public void insert( long value ) {
      a[nElems] = value;
      nElems++;
   }

  /**
   * Method to delete a value from the array
   */
   public boolean delete( long value ) {
      int j;
      for( j = 0; j < nElems; j++) {
         if( value == a[j] ) {
            break;
         }
      }
      if( j == nElems ) {
         return false;
      } else {
         for( int k = j; k < nElems; k++) {
            a[k] = a[k+1];
         }
         nElems--;
         return true;
      }
   }

  /**
   * Method to display the contents of the array
   */
   public void display() {
      for( int j = 0; j < nElems; j++) {
         System.out.print( a[j] + " " );
      }
      System.out.println( "\n  length of array: " + a.length );
   }

  /**
   * Method to find the maximum value in the contents of the array
   *   part of homework01
   */
   public long getMax() {
      long max = a[0];
      for( int j = 0; j < nElems; j++) {
         if( a[j] > max ) {
            max = a[j];
         }
      }
      return max;
   }

  /**
   * Method to find the maximum value in the contents of the array
   *   part of homework01
   *  NOTE: this is one way to do this; other ways are fine, too
   *        for example, replacing duplicates with -999 or moving
   *        contents down to "cover up" a duplicate
   */
   public void noDups() {
      Set<Long> b = new HashSet<Long>();

      for( int i = 0; i < a.length; i++ ) {
         b.add( Long.valueOf( a[i] ) );
      }
      for( long l : a ) {
         b.add( Long.valueOf( l ) );
      }
      a = new long[a.length];
      int i = 0;
      for( Long l : b ) {
         a[i++] = l.longValue();
      }
      nElems = b.size();
   }

}
