/**
 * file:  BigOhCompare.java
 * purpose: demonstrate the point at which two algorithms switch speed
 * @author: Dr. Johnson
 * @date:   2021-07-28
 * description: Given two algorithms of Big-Oh( 8n log n ) and Big-Oh( 0.01 n^2 )
 *       find the point at which the slower one becomes the faster one
 *
 */


public class BigOhCompare {

   private static double dataSetSize = 0.0;

   public static void main( String[] args ) {

      if( 0 == args.length ) {
         System.out.println( "\n\n   Sorry, you must enter a data set size value." );
         System.out.println( "   Please try again.\n\n" );
         System.exit( -1 );
      }

      try {
         dataSetSize = Double.parseDouble( args[0] );
      }
      catch( NumberFormatException nfe ) {
          System.out.println( "\n\n   Sorry, you must enter a numeric value." );
          System.out.println( "   Please try again.\n\n" );
          System.exit( -1 );
      }
      System.out.println( "\n\n   Big-Oh( 8n log n)  is: " + (8 * dataSetSize * Math.log10( dataSetSize )) );
      System.out.println( "   Big-Oh( 0.01 n^2 ) is: " + (0.01 * dataSetSize * dataSetSize) );

      System.exit( 0 );
   }
}
