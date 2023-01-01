/**
 * filename: AbstractClassUser.java
 * purpose: demonstrate the use of abstract classes
 * author: Dr. Johnson
 * date: 2020-08-18
 *
 *  Abstract classes compared to interfaces
 *  =======================================
 *    An abstract class is a class that is declared abstract—it may or may
 *    not include abstract methods. Abstract classes cannot be instantiated,
 *    but they can be subclassed.
 *    An abstract method is a method that is declared without an implementation
 *    (without braces, and followed by a semicolon).
 *    If a class includes abstract methods, then the class itself must be
 *    declared abstract
 *    When an abstract class is subclassed, the subclass usually provides
 *    implementations for all of the abstract methods in its parent class.
 *    However, if it does not, then the subclass must also be declared abstract.
 *    Abstract classes are similar to interfaces. You cannot instantiate them,
 *    and they may contain a mix of methods declared with or without an
 *    implementation. However, with abstract classes, you can declare fields
 *    that are not static and final, and define public, protected, and private
 *    concrete methods. With interfaces, all fields are automatically public,
 *    static, and final, and all methods that you declare or define (as default
 *    methods) are public. In addition, you can extend only one class, whether
 *    or not it is abstract, whereas you can implement any number of interfaces.
 *
 *    Which should you use, abstract classes or interfaces?
 *    =====================================================
 *    Consider using abstract classes if any of these statements apply to your
 *    situation:
 *       +  You want to share code among several closely related classes.
 *       +  You expect that classes that extend your abstract class have many
 *             common methods or fields, or require access modifiers other
 *             than public (such as protected and private).
 *       +  You want to declare non-static or non-final fields. This enables
 *             you to define methods that can access and modify the state of
 *             the object to which they belong.
 *    Consider using interfaces if any of these statements apply to your
 *    situation:
 *       +  You expect that unrelated classes would implement your interface.
 *             For example, the interfaces Comparable and Cloneable are
 *             implemented by many unrelated classes.
 *       +  You want to specify the behavior of a particular data type, but not
 *             concerned about who implements its behavior.
 *       +  You want to take advantage of multiple inheritance of type.
 *
 */

public class AbstractClassUser {

   private static final int BLUE = 1;
   private static final int RED  = 2;

   public AbstractClassUser() {
      System.out.println( "\n  AbstractClassUser constructor is called." );
   }

   public static void main( String [] args ) {
      AbstractClassUser acu = new AbstractClassUser();
      Square s = new Square( 23 );
      Circle c = new Circle();
      c.setColor( BLUE );

   }
}
