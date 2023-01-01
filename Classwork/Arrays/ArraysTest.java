/**
 *  filename: ArraysTest.java
 *  purpose: demonstrate some stuff with arrays
 *  author: Dr. Johnson
 *  date: 2020-08-21
 *
 *  The problem is to determine if one array of integers is a "rotation" of another array.
 *  For example, if the first array is "1, 2, 3, 4, 5" and the second array is "4, 5, 1, 2, 3"
 *  then the second array is a rotation, moving the last two elements of the first array from
 *  the end to the beginning of the array, maintaining the order.
 *
 *  The solution method is to double the first array, concatenating the two copies.  If the
 *  second array is a rotation, it will appear SOMEWHERE in the doubled array.  The trick in
 *  this case is to turn the arrays into strings, then remove the brackets that are added by
 *  the Arrays.toString() method.  Then, use the String.contains() method to see if s2 is
 *  contained by s1s1.
 *
 *  From "Cracking the Coding Interview" by Gayle McDowell; ISBN 978-0-9847828-0-2
 *
 *  NOTE: the original problem was implemented with strings, not integer arrays; this was
 *  adapted for CMSI 281 as an Array exercise
 */

import java.util.Arrays;

public class ArraysTest {

   public static void main( String [] args ) {

      int[] a = { 2, 3, 5, 7, 9, 11, 13, 17, 19, 23 };
      int[] b = { 19, 23, 2, 3, 5, 7, 9, 11, 13, 17 };
      int[] c = { 17, 19, 23, 2, 3 };
      int[] d = { 17, 23, 29, 31 };
      
      System.out.println( "\n  a: " + Arrays.toString( a ) );
      String s1 = Arrays.toString( a );
      
      StringBuilder s1s1 = new StringBuilder( Arrays.toString( a ) + Arrays.toString( a ) );
      System.out.println( "  s1: " + s1 );
      System.out.println( "  s1s1: " + s1s1.toString() );
      
      int bracket = s1s1.indexOf( "]" );
      System.out.println( "  bracket index: " + bracket );
      s1s1.replace( bracket, bracket + 2, ", " );
      
      s1 = s1s1.substring( 1, s1s1.length() - 1 );
      System.out.println( "  s1s1: " + s1s1.toString() );
      System.out.println( "  s1: " + s1 );
      
      String s2 = Arrays.toString( b );
      s2 = s2.substring( 1, s2.length() - 1 );
      System.out.println( "  s2: " + s2 );
      System.out.println( "  s2 is rotation of s1? expeting true, got: " + (s1.contains( s2 ) ? "true" : "false") + "\n" );
      
      s2 = Arrays.toString( c );
      s2 = s2.substring( 1, s2.length() - 1 );
      System.out.println( "  s2: " + s2 );
      System.out.println( "  s2 is rotation of s1? expeting true, got: " + (s1.contains( s2 ) ? "true" : "false") + "\n" );
      
      s2 = Arrays.toString( d );
      s2 = s2.substring( 1, s2.length() - 1 );
      System.out.println( "  s2: " + s2 );
      System.out.println( "  s2 is rotation of s1? expeting false, got: " + (s1.contains( s2 ) ? "true" : "false") + "\n" );

   }

}
