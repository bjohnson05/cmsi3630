/**
 * filename: IntStack.java
 * purpose: Int Linked List Stack Implementation Demonstrator
 * @author: B.J. Johnson
 * @date: 2018-09-26
 * @version: 1.0.0
 */
public class IntStack {

   IntLinkedList myStack;

   IntStack() {
      myStack = new IntLinkedList();         // constructor
   }

   public void push( int itemToPush ) {
      myStack.prepend( itemToPush );
   }

   public int peek() throws EmptyStackException {
      if( myStack.getSize() != 0 ) {
         return myStack.getIteratorAt( 0 ).getCurrentInt();     // we use the iterator
      } else {
         throw new EmptyStackException( "   Oops, the stack is empty..." );
      }
   }

   public int pop() {
      return myStack.removeAt( 0 );
   }

}
