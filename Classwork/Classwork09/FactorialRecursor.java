/**
 * filename: FactorialRecursor.java
 * purpose: demonstrate recursion using factorial
 * @author: Dr. Johnson
 * @date: 2020-10-25
 */

public class FactorialRecursor {
   public int factorial( int n ) {
      System.out.println( "N is: " + n );
      if( n == 0 ) {
         return 1;
      } else {
         return (n * factorial( n - 1 ));
      }
   }

   public static void main( String[] args ) {
      FactorialRecursor fr = new FactorialRecursor();
      int count = Integer.parseInt( args[0] );
      System.out.println( "The value of " + count + "! is: " + fr.factorial( count ) );
      System.exit( 0 );
   }
}

