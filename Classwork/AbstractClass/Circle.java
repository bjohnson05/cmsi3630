/**
 *  filename: Circle.java
 *  purpose: extend the AbstractShape class
 *  author: Dr. Johnson
 *  date: 2020-08-18
 */

public class Circle extends AbstractShape {

   private double radius = 0.0;

   public Circle(  ) {
      System.out.println( "\n  The extended class 'Circle' constructor is called." );

   }

   public double getArea() {
      return Math.PI * radius * radius;
   }

}
