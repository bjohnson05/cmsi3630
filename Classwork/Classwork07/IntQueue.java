/**
 * filename: IntQueue.java
 * purpose: Int Linked List Stack Implementation Demonstrator
 * @author: B.J. Johnson
 * @date: 2018-09-26
 * @version: 1.0.0
 */
public class IntQueue {

   public IntLinkedList myQueue;

   IntQueue() {
      myQueue = new IntLinkedList();         // constructor
   }

   public void enQueue( int itemToPush ) {
      myQueue.prepend( itemToPush );
   }

   public int peek() {
      return myQueue.getIteratorAt( 0 ).getCurrentInt();     // we use the iterator
   }

   public int deQueue() {
      return myQueue.removeAt( myQueue.getSize() - 1 );
   }

}
