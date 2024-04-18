/*
 * File name: PriorityQTester.java
 * Purpose  : demonstrates one way to do a Priority queue using a Heap
 * @author  : B.J. Johnson
 * @date    : 2018-11-04
 * @version : 1.0.0
 *
 * Description:  Implement the PriorityQ class in the PriorityQ.java program
 *                (Listing 4.6 in Lafore book) using a heap instead of an array.
 *                You should be able to use the Heap class in the heap.java
 *                program (Listing 12.1) without modification.  Make it a
 *                descending queue (largest item is removed).
 * NOTE: for this exercise, I simply took the Heap class from the Lafore book
 *       and implemented it, then used it in the PriorityQ class.  I changed the
 *       type long array in the priority queue to be a Heap.  Some modifications
 *       were needed to the PriorityQ methods to call the Heap methods, using the
 *       PQ methods as wrappers.  Also had to add a couple of methods to the Heap
 *       class to implement things like peek() and isFull() so the tests in this
 *       file match the ones that were in the original file.  This file can then
 *       remain unchanged from the HeapNode array implementation, and still works
 *       properly, with the Heap being a max heap.
 */
import java.io.IOException;

public class PriorityQTester {

   public static void main( String[] args ) throws IOException {
      PriorityQ thePQ = new PriorityQ( 50 );
      System.out.println( "" );
      System.out.println( "  New Priority Queue ['PQ'] created with space for 50 items." );
      System.out.println( "  Checking if PQ is empty, should be 'true': " + thePQ.isEmpty() + "\n" );

      thePQ.insert( new HeapNode( 30 ) );
      thePQ.insert( new HeapNode( 50 ) );
      thePQ.insert( new HeapNode( 10 ) );
      thePQ.insert( new HeapNode( 40 ) );
      thePQ.insert( new HeapNode( 20 ) );
      thePQ.insert( new HeapNode( 35 ) );
      thePQ.insert( new HeapNode( 45 ) );
      thePQ.insert( new HeapNode( 15 ) );
      thePQ.insert( new HeapNode( 25 ) );
      thePQ.insert( new HeapNode(  5 ) );
      System.out.println( "  Priority Queue loaded with 10 items in order 30,50,10,40,20,35,45,15,25,5" );
      System.out.println( "  Higher numbers have higher priority [max heap]....\n" );
      System.out.println( "  Checking if PQ is full, should be 'false': " + thePQ.isFull() + "\n" );

      System.out.println( "  Peeking at maximum [root] value should be '50': " + thePQ.peekMin().getKey() + "\n" );

      System.out.print( "\n  PriorityQ representation: " );
      thePQ.displayPQ();

      System.out.println( "\n  Removing one item: " );
      HeapNode item = thePQ.remove();
      System.out.print( "    item removed: " + item.getKey() );
      System.out.print( "\n  PriorityQ representation: " );
      thePQ.displayPQ();

      System.out.println( "\n  Removing a second item: " );
      item = thePQ.remove();
      System.out.print( "    item removed: " + item.getKey() );
      System.out.print( "\n  PriorityQ representation: " );
      thePQ.displayPQ();

      System.out.print( "\n  Removing items from PQ in priority order: \n    " );
      while( !thePQ.isEmpty() ) {
         item = thePQ.remove();
         System.out.print( item.getKey() + " " );          // should output 40 35 30 25 20 15 10 5
      }
      System.out.println( "\n\n  Checking if PQ is empty, should be 'true': " + thePQ.isEmpty() + "\n" );
      System.out.println("  . . . test completed . . .");
   }

}
