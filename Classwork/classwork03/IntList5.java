/**
 *  IntList5
 *  Fourth version of sample code from week03.html
 */

public class IntList5 implements IntListInterface {
   private int[] theList;
   private int   size;

   private static final int STARTING_SIZE = 19;    // defines starting size of the list

   private class ListException extends Exception {
      public ListException( String m ) {
         super( m );
      }
   }

   public IntList5() {
      theList = new int[STARTING_SIZE];
      size = 0;
   }

   public int getValueAtIndex( int index ) {
      try {
         if( size == 0 ) {
            throw new ListException( "The list is empty!" );
         } else if( index > size ) {
            throw new ListException( "The index value is too large" );
         } else if( index < 0 ) {
            throw new ListException( "The index value is too small");
         }
      }
      catch( ListException le ) {}
      return theList[index];
   }

}
