/**
 * this is LISTING 4.6 The priorityQ.java Program from Lafore
 * PriorityQApp.java
 * demonstrates priority queue
 * to run this program: C>java Lafore46App
 */

import java.io.IOException;

class Lafore46App {
   public static void main( String[] args ) throws IOException {
      Lafore46 thePQ = new Lafore46( 5 );
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
