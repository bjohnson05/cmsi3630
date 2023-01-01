/**
 * filename: IntStackTester.java
 * purpose: Tests for the Int Linked List Stack Implementation Demonstrator
 * @author: B.J. Johnson
 * @date: 2018-09-26
 * @version: 1.0.0
 */

   public class IntStackTester {

      public static void main( String[] args ) {
         IntStack testStack = new IntStack();
         System.out.println( "\n   Testing IntLinkedList-based Stack Application\n" );
         testStack.push( 19 );
         testStack.push( 23 );
         testStack.push( 29 );
         testStack.push( 31 );
         testStack.push( 37 );
         testStack.push( 41 );
         testStack.push( 43 );
         testStack.push( 47 );
         testStack.push( 51 );
         testStack.push( 59 );
         try {
            System.out.println( "  Pushed values 59, 51, 47, 43, 41, 37, 31, 29, 23, and 19\n" );
            System.out.println( "  Testing peek() and pop() methods..." );
            System.out.println( "      Peek at the top of the stack: " + testStack.peek() );      // 57
            System.out.println( "   Popping top thing: " + testStack.pop() );      // 57 removed
            System.out.println( "      Peek at the top of the stack: " + testStack.peek() );      // 51
            System.out.println( "   Popping top thing: " + testStack.pop() );      // 51 removed
            System.out.println( "      Peek at the top of the stack: " + testStack.peek() );      // 47
            System.out.println( "   Popping top thing: " + testStack.pop() );      // 47 removed
            System.out.println( "      Peek at the top of the stack: " + testStack.peek() );      // 43
            System.out.println( "   Testing adding values of two pops and pushing result ~ expected 84" );
            testStack.push( testStack.pop() + testStack.pop() );
            System.out.println( "      Peek at the top of the stack: " + testStack.peek() );      // what'll it be?
            System.out.println( "   Popping top thing: " + testStack.pop() );      // now it's removed
            System.out.println( "      Peek at the top of the stack: " + testStack.peek() );      // 37
            System.out.println( "   Popping top thing: " + testStack.pop() );      // 37 removed
            System.out.println( "      Peek at the top of the stack: " + testStack.peek() );      // 31
            System.out.println( "   Popping top thing: " + testStack.pop() );      // 31 removed
            System.out.println( "      Peek at the top of the stack: " + testStack.peek() );      // 29
            System.out.println( "   Popping top thing: " + testStack.pop() );      // 29 removed
            System.out.println( "      Peek at the top of the stack: " + testStack.peek() );      // 23
            System.out.println( "   Popping top thing: " + testStack.pop() );      // 23 removed
            System.out.println( "      Peek at the top of the stack: " + testStack.peek() );      // 19
            System.out.println( "   Popping top thing: " + testStack.pop() );      // 19 removed
            System.out.println( "   Stack should be empty, so an exception will be thrown by the next peek()" );
            System.out.println( "      Peek at the top of the stack: " + testStack.peek() );      // 43
         }
         catch( EmptyStackException ese ) {
            System.out.println( ese.getLocalizedMessage() );
         }
      }

   }
