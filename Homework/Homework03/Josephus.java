/**
 * filename: Josephus.java
 * purpose : demonstrates the Josephus puzzle
 * @author : B.J. Johnson
 * @date   : 2018-10-20
 * @version: 1.0.0
 */

public class Josephus extends CircularIntLinkedList {

   private int count = 3;
   private int total = 20;

  /**
   * CONSTRUCTOR
   *   Handles all the [rudimentary] error checks and just quits if error
   */
   public Josephus( String maxPeople, String countBy ) {
      total = Integer.parseInt( maxPeople );
      count = Integer.parseInt( countBy );
      if( (total < 1) || (count < 1) ) {
         System.out.println( "\n\n  There must be some people and/or a counting number...." );
         System.out.println( "   Please try again! " );
         System.exit( -1 );
      }
      if( count > total ) {
         System.out.println("\n\n   Can't count a person index bigger than the total...." );
         System.out.println( "   Please try again! " );
         System.exit( -1 );
      }
      if( total == 1 ) {
         System.out.println( "\n\n   The Romans are evil: THE ONE PERSON DIES!!" );
         System.out.println( "   Please try again! " );
         System.exit( -1 );
      }
   }

   public static void main( String[] args ) {

      if( 0 == args.length ) {
         System.out.println( "\n   Usage: java Josephus <#people> <count#>" );
         System.exit( 0 );
      }

     // initialize things
      Josephus j = new Josephus( args[0], args[1] );
      System.out.println( "\nJosephus problem with " + j.total + " people, counting by " + j.count + "..." );
      for( int i = 1; i <= j.total; i++ ) {
         j.insert( i );
      }
      j.it.next();  // moves back to the "1" Node
      j.display();
      System.out.println( "\n beginning count down....");
      System.out.println( "     starting count at current node: " + j.it.getCurrentInt() );
      while( j.getSize() > 1 ) {
         for( int i = 0; i < (j.count - 1); i++ ) {
            j.it.next();
            System.out.println( "     ... current node: " + j.it.getCurrentInt() );
         }
         System.out.println( "   person " + j.remove() + " commits suicide." );
         if( (args.length > 2) && (args[2].equals( "true" )) ) {
             System.out.print( "\tlist is now:" );
            j.display();
         } else {
            System.out.println();
         }
      }

      System.out.println( "\n\nRemaining person is at node: " + j.it.getCurrentInt() );
      System.exit( 0 );
   }
}
