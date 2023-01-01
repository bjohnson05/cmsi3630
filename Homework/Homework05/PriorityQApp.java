/**
 * this is LISTING 4.6 The PriorityQApp.java Program from Lafore
 * save this file to PriorityQApp.java
 * demonstrates priority queue
 * to run this program: %> java Lafore46App
 */

import java.io.IOException;

class PriorityQApp {
   public static void main( String[] args ) throws IOException {
      PriorityQ thePQ = new PriorityQ( 5 );
      thePQ.insert( 30 );
      thePQ.insert( 50 );
      thePQ.insert( 10 );
      thePQ.insert( 40 );
      thePQ.insert( 20 );
      while( !thePQ.isEmpty() ) {
         long item = thePQ.remove();
         System.out.print( item + " " ); // 10, 20, 30, 40, 50
      }
      System.out.println( "" );
   }
}
