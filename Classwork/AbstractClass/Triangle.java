/**
 *  filename: Triangle.java
 *  purpose: extend the AbstractShape class
 *  author: Dr. Johnson
 *  date: 2020-08-18
 */

public class Triangle extends AbstractShape {

   private double base = 0.0;
   private double height = 0.0;

   public Triangle( int s1, int s2, int s3 ) {
      System.out.println( "\n  The extended class 'Triangle' constructor is called." );

   }

   public double getArea() {
      return 0.5 * base * height;
   }

}
