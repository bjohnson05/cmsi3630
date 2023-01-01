/**
 *  filename: Square.java
 *  purpose: extend the AbstractShape class
 *  author: Dr. Johnson
 *  date: 2020-08-18
 */

public class Square extends Rectangle {

   public Square( int s ) {
      super( s, s );
      System.out.println( "\n  The extended class 'Square' constructor is called." );
   }

}
