/*
 * filename: IntLinkedListTester.java
 * purpose: Tests the singly linked list data structure
 */

   public class IntLinkedListTester {

      public static void main( String[] args ) {
         IntLinkedList myList = new IntLinkedList();
         System.out.println( "\n   Inserting values into new list: " );
         myList.prepend( 59 );
         myList.prepend( 57 );
         myList.prepend( 53 );
         myList.prepend( 51 );
         myList.prepend( 47 );
         myList.prepend( 43 );
         myList.prepend( 41 );
         myList.prepend( 37 );
         myList.prepend( 31 );
         myList.prepend( 29 );
         myList.prepend( 23 );
         myList.prepend( 19 );
         myList.prepend( 17 );
         myList.prepend( 13 );
         myList.prepend( 11 );
         myList.prepend(  7 );
         myList.prepend(  5 );
         myList.prepend(  3 );
         myList.prepend(  2 );
         System.out.println( "   Displaying current list contents....." );
         IntLinkedList.Iterator myIt = myList.getIteratorAt( 0 );
         while( myIt.hasNext() ) {
            System.out.println( "Current Node is: " + myIt.getCurrentInt() );
            myIt.next();
         }
         System.out.println( "Current Node is: " + myIt.getCurrentInt() );
         System.out.println( "\n\n   Testing new 'insertAt()' and 'removeAt()' methods" );
         System.out.println( "   Inserting 1001 at index 11...." );
         myList.insertAt( 11, 1001 );
         System.out.println( "   Displaying current list contents....." );
         myIt = myList.getIteratorAt( 0 );
         while( myIt.hasNext() ) {
            System.out.println( "Current Node is: " + myIt.getCurrentInt() );
            myIt.next();
         }
         System.out.println( "Current Node is: " + myIt.getCurrentInt() );
         System.out.println( "\n   Removing node at index 16...." );
         int valueRemoved = myList.removeAt( 16 );
         System.out.println( "   Displaying current list contents....." );
         myIt = myList.getIteratorAt( 0 );
         while( myIt.hasNext() ) {
            System.out.println( "Current Node is: " + myIt.getCurrentInt() );
            myIt.next();
         }
         System.out.println( "Current Node is: " + myIt.getCurrentInt() );
         System.out.println( "\n   Value of removed node: " + valueRemoved );

         System.out.println( "\n   Inserting 101 at index 5...." );
         myList.insertAt( 5, 101 );
         System.out.println( "   Displaying current list contents....." );
         myIt = myList.getIteratorAt( 0 );
         while( myIt.hasNext() ) {
            System.out.println( "Current Node is: " + myIt.getCurrentInt() );
            myIt.next();
         }
         System.out.println( "Current Node is: " + myIt.getCurrentInt() );

      }
   }
