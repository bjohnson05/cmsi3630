/**
 * this is LISTING 4.6 The priorityQ.java Program from Lafore
 * copy this code and name the file PriorityQ.java
 *   then rename the class PriorityQ
 * demonstrates priority queue
 * to run this program: %> java PriorityQApp
 */
class PriorityQ {
  // array in sorted order, from max at 0 to min at size-1
   private int maxSize;
   private long[] queArray;
   private int nItems;

  // constructor
   public PriorityQ(int s) {
      maxSize = s;
      queArray = new long[maxSize];
      nItems = 0;
   }

  // insert item
   public void insert( long item ) {
      int j;
      if( nItems == 0 ) {           // if no items,
         queArray[nItems++] = item; // insert at 0
      } else {
         for( j = nItems - 1; j >= 0; j-- ) {
            if( item > queArray[j] ) {
               queArray[j+1] = queArray[j];
            } else {
               break; // done shifting
            }
         }
         queArray[j+1] = item; // insert it
         nItems++;
      }
   }

  // remove the minimum item
   public long remove() {
      return queArray[--nItems];
   }

  // peek at the minimum item
   public long peekMin() {
      return queArray[nItems-1];
   }

  // check for empty queue
   public boolean isEmpty() {
      return (nItems==0);
   }

  // check for full queue
   public boolean isFull() {
      return (nItems == maxSize);
   }
}
