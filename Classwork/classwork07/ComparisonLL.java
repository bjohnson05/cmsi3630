/**
 * filename: ComparisonLL.java
 * purpose:  demonstrate linked list vs array list
 * author:   Dr. Johnson
 * date:     2023-02-19
 */

import java.util.LinkedList;

public class ComparisonLL {

   private static int TEST_SIZE = 200000;

   public ComparisonLL() {
      super();
   }

  // here's the method from the web page
   public void testArrayListPrepend() {
      LinkedList<String> myRA = new LinkedList<String>();
      for( int i = 0; i < TEST_SIZE; i++ ) {
         myRA.add( 0, "" + i );
      }
   }

  // a main to call the method and output the elapsed time
   public static void main( String [] args ) {

      ComparisonLL cll = new ComparisonLL();
      long start = System.currentTimeMillis();
      cll.testArrayListPrepend();
      long end = System.currentTimeMillis();
      long minutes = (end - start) / 1000;
      long seconds = ((end - start) % 1000) % 60;
      if( seconds >= 60 ){
         seconds %= 60;
         minutes++;
      }
      System.out.println( "\n   Elapsed time: " + minutes + " minutes and " + seconds + " seconds.\n" );
   }
}
