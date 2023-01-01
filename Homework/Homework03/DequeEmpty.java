/*
 *  File name: Deque.java
 *  Purpose  : implements a Deque using an array
 *  @author  : Dr. Johnson
 *  @date    : 2018-09-27
 *  @version : 1.0.0
 *  NOTES    : In this implementation, the "front" of the Deque will be considered
 *             to be the "left end", making the "rear" of the Deque the "right end".
 *
 *             Remember that a Deque is double-ended, so insertions and deletions
 *             may occur at either end.  It's a "FLIFLO" structure.
 *             ....or maybe "FOLIFOLO".....
 *
 *             Implemented with an array of long primitives
 */

class DequeEmpty {
   private int    maxSize;       // max size at creation
   private long[] dequeArray;    // the underlying storage
   private int    front;         // let's call this "left"

   private int    rearLeft;      // new way of looking at this ~ front is actually right
   private int    rearRight;     //    this makes things work more like what we expect

  /**
   *  constructor
   *  @param s int for the size of the underlying array
   */
   public DequeEmpty( int s ) {
      maxSize = s;
      dequeArray = new long[maxSize];
      nItems = 0;

      rearLeft    =  maxSize - 1;
      rearRight   =  0;
   }

  /**
   *  put item at rear of deque
   *  @param j long primitive containing the value to insert
   */
   public void insertLeftNew( long j ) {
      if( nItems == maxSize ) {
         // full message
      } else {
         // decrement rear and insert
         // one more item
      }
   }

  /**
   *  put item at front of deque
   *  @param j long primitive containing the value to insert
   */
   public void insertRightNew( long j ) {
      if( nItems == maxSize ) {
         // full message
      } else {
         System.out.println( "     ...inserting " + j + " at [" + frontRight + "]" );
         // increment rear and insert
         // one more item
      }
   }

  /**
   *  remove item at front of deque
   *  @return long primitive containing the value removed
   */
   public long removeLeftNew() {
      long temp = 0;
      if( getSize() == 0 ) {
         // empty message
      } else {
         // one less item
         // save curremt location in temp
         // set current location to zero to clear it out
      }
      return temp;                              // return it
   }

  /**
   *  remove item at rear of deque
   *  @return long primitive containing the value removed
   */
   public long removeRightNew() {
      long temp = 0;
      if( getSize() == 0 ) {
         // empty message
         return 0;
      } else {
         // one less item
         // save curremt location in temp
         // set current location to zero to clear it out
      }
      return temp;                              // return it
   }

  /**
   *  peek at front of deque
   *  @return long primitive containing the value peeked at
   */
   public long peekFront()
   {
      return dequeArray[rearLeft];
   }

  /**
   *  peek at back of deque
   *  @return long primitive containing the value peeked at
   */
   public long peekBack()
   {
      return dequeArray[rearRight];
   }

  /**
   *  determine if the deque is empty
   *  @return boolean primitive containing true if deque is empty
   */
   public boolean isEmpty() {
      return ( nItems == 0 );
   }

  /**
   *  determine if the deque is full
   *  @return boolean primitive containing true if deque is full
   */
   public boolean isFull() {
      return ( nItems == maxSize );
   }

  /**
   *  determine number of items in deque
   *  @return int primitive containing item count
   */
   public int getSize() {
      return nItems;
   }

  /**
   *  display the contents of the deque AS AN ARRAY
   *     note this is NOT NECESSARILY as a "Dequq" view!
   */
   public void displayDequeArrayContents( boolean displayIndices ) {
      if( displayIndices ) {
         System.out.println( " rearLeft : " + rearLeft  + "  rearRight: " + rearRight );
      }
      for( long i : dequeArray ) {
         System.out.print( "[" + i + "]" );
      }
      System.out.println( "" );
   }
}
