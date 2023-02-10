/**
 *  IntList2
 *  Second version of sample code from week03.html
 */

public class IntList2 implements IntListInterface {
   private int[] theList;
   private int   size;

   private static final int STARTING_SIZE = 19;    // defines starting size of the list

   public IntList2() {
      theList = new int[STARTING_SIZE];
      size = 0;
   }

}
