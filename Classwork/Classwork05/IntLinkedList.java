/*
 * filename: IntLinkedList.java
 * purpose: demonstrates a singly linked list data structure
 */

   public class IntLinkedList {

      private Node head;
      private int  size;

     // the constructor
      IntLinkedList() {
         head = null;
         size = 0;
      }

      public int getSize() {
         return size;
      }

      public void prepend( int dataToAdd ) {
         Node currentHead = head;
         head = new Node( dataToAdd );
         head.next = currentHead;
         size++;
      }

      public Iterator getIteratorAt( int index ) {
         if( (index > size) || (index < 0) ) {
            throw new IllegalArgumentException();
         }
         Iterator it = new Iterator();
         while( index > 0 ) {
            it.next();
            index--;
         }
         return it;
      }

/**
 *  insertAt() takes an integer index location and a data value and
 *    inserts a node with that data BEFORE the node at that index.
 */
      public void insertAt( int index, int dataValue ) {
         if( index == 0 ) {
            prepend( dataValue );
            return;
         }
         Iterator thisIsIt = getIteratorAt( index - 1 );
         Node newNode = new Node( dataValue );
         newNode.next = thisIsIt.currentNode.next;
         thisIsIt.currentNode.next = newNode;
         size++;
      }

/**
 *  removeAt() takes an integer index location ONLY, and removes the
 *    node at that index.
 */
      public int removeAt( int index ) {
         Iterator it = null;
         int valueRemoved;
         if( index == 0 ) {
            it = getIteratorAt( 0 );
            valueRemoved = it.currentNode.data;
            head = it.currentNode.next;
         } else {
            it = getIteratorAt( index - 1 );
            valueRemoved = it.currentNode.next.data;
            it.currentNode.next = it.currentNode.next.next;
         }
         size--;
         return valueRemoved;
      }

/**
 * The internal Node class; each node has a data field that
 *    stores an int, and a Node field that stores a reference
 *    to the next node in the list
 */
      private class Node {

         int data;            // remember this is an IntLinkedList
         Node next;           // here's the self-referential part

         // constructor
         Node( int d ) {
            data = d;
            next = null;
         }
      }

/**
 * The internal Iterator class; this provides the ability to
 *    go through all the nodes in the list, starting at any
 *    node you choose, and also allows visibility of the value
 *    at the list item that is currently being referred to by
 *    the Iterator's internal 'currentNode' object
 */
      public class Iterator {
         private Node currentNode;

         Iterator() {
            currentNode = head;
         }

         public void next() {
            if( currentNode == null ) {
               return;
            } else {
               currentNode = currentNode.next;
            }
         }

         public boolean hasNext() {
            return ((currentNode != null) && (currentNode.next != null));
         }

         public int getCurrentInt() {
            return currentNode.data;
         }

      }
   }
