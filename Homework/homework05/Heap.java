/*
 * File name: Heap.java
 * Purpose  : helper that demonstrates one way to do a Priority queue
 * @author  : B.J. Johnson
 * @date    : 2018-11-23
 * @version : 1.0.0
 *
 * Description:  Implement the PriorityQ class in the PriorityQ.java program
 *                (Listing 4.6 in Lafore book) using a heap instead of an array.
 *                You should be able to use the Heap class in the heap.java
 *                program (Listing 12.1) without modification.  Make it a
 *                descending queue (largest item is removed).
 *
 */

import java.io.*;

class HeapNode {

   private int iData;

   public HeapNode( int key ) {
      iData = key;
   }

   public int getKey() {
      return iData;
   }

   public void setKey( int id ) {
      iData = id;
   }

}

class Heap {

   private HeapNode[]   heapArray;
   private int          maxSize;
   private int          currentSize;

   public Heap( int max ) {
      maxSize = max;
      currentSize = 0;
      heapArray = new HeapNode[maxSize]; // create array
   }

   public boolean isEmpty() {
      return currentSize == 0;
   }

   public boolean isFull() {
      return currentSize == maxSize;
   }

   public boolean insert( int key ) {
      if( currentSize==maxSize ) {
         return false;
      }
      HeapNode newNode = new HeapNode( key );
      heapArray[currentSize] = newNode;
      trickleUp( currentSize++ );
      return true;
   }

   public void trickleUp( int index ) {
      int parent = (index-1) / 2;
      HeapNode bottom = heapArray[index];
      while( (index > 0) && (heapArray[parent].getKey() < bottom.getKey()) ) {
         heapArray[index] = heapArray[parent]; // move it down
         index = parent;
         parent = (parent-1) / 2;
      }
      heapArray[index] = bottom;
   }

   public HeapNode peek() {
      return heapArray[0];
   }

   public HeapNode remove() {
      HeapNode root = heapArray[0];
      heapArray[0] = heapArray[--currentSize];
      trickleDown( 0 );
      return root;
   }

   public void trickleDown( int index ) {
      int largerChild;
      HeapNode top = heapArray[index]; // save root
      while( index < currentSize / 2 ) { //  // while HeapNode has at least one child,
         int leftChild = 2 * index + 1;
         int rightChild = leftChild + 1;
         // see if rightChild exists and find larger child
         if( (rightChild < currentSize) && (heapArray[leftChild].getKey() < heapArray[rightChild].getKey()) ) {
            largerChild = rightChild;
         } else {
            largerChild = leftChild;
         }
         // is the top >= largerChild?
         if( top.getKey() >= heapArray[largerChild].getKey() ) {
            break;
         }
         heapArray[index] = heapArray[largerChild];   // shift child up
         index = largerChild;
      }
      heapArray[index] = top; // root to index
   }

   public boolean change( int index, int newValue ) {
      if( (index < 0) || (index >= currentSize) ) {
         return false;
      }
      int oldValue = heapArray[index].getKey();    // remember old
      heapArray[index].setKey(newValue);           // change to new
      if( oldValue < newValue ) {                  // if raised,
         trickleUp( index );                       // trickle it up
      } else {                                     // if lowered,
         trickleDown(index);                       // trickle it down
      }
      return true;
   }

   public void displayHeap() {
      System.out.print( "heapArray: " ); // array format
      for( int m = 0; m < currentSize; m++ ) {
         if( heapArray[m] != null ) {
            System.out.print( heapArray[m].getKey() + " " );
         } else {
            System.out.print( "-- ");
         }
      }
      System.out.println();

      // heap format
      int nBlanks = 32;
      int itemsPerRow = 1;
      int column = 0;
      int j = 0;           // current item
      String dots = "...............................";
      System.out.println( dots + dots );

      while( currentSize > 0 ) {
         if( column == 0 ) {         // first item in row?
            for( int k = 0; k < nBlanks; k++ ) {   // preceding blanks
               System.out.print(' ');
            }
         }
         System.out.print( heapArray[j].getKey() );      // display item
         if( ++j == currentSize ) {                      // done?
            break;
         }
         if( ++column == itemsPerRow ) {                 // end of row?
            nBlanks /= 2;                    // half the blanks
            itemsPerRow *= 2;                // twice the items
            column = 0;                      // start over on
            System.out.println();            // new row
         } else {                            // next item on row
            for(int k = 0; k < nBlanks * 2 - 2; k++ ) {
               System.out.print(' ');        // interim blanks
            }
         }
      }
      System.out.println("\n" + dots + dots ); // dotted bottom line
   }

}
