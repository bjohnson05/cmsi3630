/*
 * File name: PriorityQ.java
 * Purpose  : demonstrates one way to do a Priority queue
 * @author  : B.J. Johnson
 * @date    : 2018-11-04
 * @version : 1.0.0
 *
 * Description:  Implement the PriorityQ class in the PriorityQ.java program
 *                (Listing 4.6 in Lafore book) using a heap instead of an array.
 *                You should be able to use the Heap class in the heap.java
 *                program (Listing 12.1) without modification.  Make it a
 *                descending queue (largest item is removed).
 *
 */
import java.io.IOException;

public class PriorityQ {

   // array in sorted order, from max at 0 to min at size-1
   private int          maxSize;
   private Heap         queArray;
   private int          nItems;
   private static final int MAX_SIZE = 50;

   public PriorityQ(int s) {
      maxSize  = s;
      queArray = new Heap( MAX_SIZE );
      nItems   = 0;
   }

   public void insert( HeapNode item ) {
      queArray.insert( item.getKey() );
   }

   public HeapNode remove() {           // remove minimum item
      return queArray.remove();
   }

   public HeapNode peekMin() {          // peek at minimum item
      return queArray.peek();
   }

   public boolean isEmpty() {       // true if queue is empty
      return queArray.isEmpty();
   }

   public boolean isFull() {        // true if queue is full
      return queArray.isFull();
   }

   public void displayPQ() {
      queArray.displayHeap();
   }
}
