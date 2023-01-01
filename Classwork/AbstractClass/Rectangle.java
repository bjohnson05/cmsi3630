/**
 *  filename: Rectangle.java
 *  purpose: extend the AbstractShape class
 *  author: Dr. Johnson
 *  date: 2020-08-18
 */

public class Rectangle extends AbstractShape {

   protected double length = 0.0;
   protected double width = 0.0;

   public Rectangle() {
      System.out.println( "\n  The extended class 'Rectangle' constructor is called." );
   }

   public Rectangle( int l, int w ) {
      System.out.println( "\n  The extended class 'Rectangle' constructor is called." );
      length = l;
      width  = w;
   }

   public double getArea() {
      return length * width;
   }
}
