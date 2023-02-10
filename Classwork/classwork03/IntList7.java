/**
 *  IntList7
 *  Fourth version of sample code from week03.html
 */

public class IntList7 implements IntListInterface {
   private int[] theList;
   private int   size;

   private static final int STARTING_SIZE = 19;    // defines starting size of the list

   private class ListException extends Exception {
      public ListException( String m ) {
         super( m );
      }
   }

   public IntList7() {
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

   public boolean append( int valueToAdd ) {
      if( size < theList.length ) {
         theList[size] = valueToAdd;
         size++;
         return true;
      } else {
         // what should we do here, if there's no room?
      }
      return false;
   }

  // we've gotta have these to actually get things to compile
   public boolean insertValueAtIndex( int value, int index ) {
     return true;
   }
   public int removeValueAtIndex( int index ) {
      return -1;
   }

   public static void main( String[] args ) {
      IntList list = new IntList();
      list.append( 2 );
      list.append( 3 );
      list.append( 5 );
      list.append( 7 );
      System.out.println( list.getValueAtIndex( 3 ) );   // should return the value 7
      System.out.println( list.getValueAtIndex( 18 ) );  // just to see what happens

   }
}
