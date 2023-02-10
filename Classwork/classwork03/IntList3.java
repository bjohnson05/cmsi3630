/**
 *  IntList3
 *  Third version of sample code from week03.html
 */

public class IntList3 implements IntListInterface {
   private int[] theList;
   private int   size;

   private static final int STARTING_SIZE = 19;    // defines starting size of the list

   public IntList3() {
      theList = new int[STARTING_SIZE];
      size = 0;
   }

   public int getValueAtIndex( int index ) {
      if( size == 0 ) {
         return -1;
      } else if( index > size ) {
         return -1;
      } else if( index < 0 ) {
         return -1;
      } else {
         return theList[index];
      }
   }

}
