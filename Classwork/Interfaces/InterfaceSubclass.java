/**
 *  filename: InterfaceSubclass.java
 *  purpose: to show how interfaces and extensions can be used to simulate
 *    polymorphism in Java which other languages [like C++ for example] allow
 *    directly
 *  author:  Dr. Johnson
 *  date:  2020-08-17
 */

public class InterfaceSubclass extends InterfaceUser implements InterfaceC {

   public InterfaceSubclass() {
      System.out.println( "\n   InterfaceSubclass object created..." );
   }

  /**
   *  these two methods are the IMPLEMENTATIONS of the methods defined in the
   *     InterfaceDemo interface
   */
   public int multiply( int a, int b ) {
      return a * b;
   }

   public double getWeight() {
      System.out.println( "      I think you weigh 175 pounds [this will appear first]" );
      return 175.0;
   }

  /**
   *  this is the main that calls the implementations
   */
   public static void main( String [] args ) {

      InterfaceSubclass ius = new InterfaceSubclass();
      System.out.println( "    Calling ius.addThree(7): expecting 10.0, got " + ius.addThree( 7.0 ) );
      System.out.println( "    Calling ius.sayHi(\"bozo\"): expecting \"done\", got " + ius.sayHi( "bozo" ) );
      System.out.println( "    Calling ius.isTrue( 0 == 0 ): expecting true, got : " + ius.isTrue( 0 == 0 ) );
      System.out.println( "    Calling ius.divideBySeven(123456.789): expecting 17,636.68414, got " + ius.divideBySeven( 123456.789 ) );
      System.out.println( "    Calling ius.getFirstChar(\"test string\"): expecting \"t\", got " + ius.getFirstChar( "test string" ) );
      System.out.println( "    Calling ius.sayMyName( \"Winifred\" ): expecting printed message : " );
      ius.sayMyName( "Winifred" );
      System.out.println( "    Calling ius.multiply( 7, 8 ): expecting 56, got " + ius.multiply( 7, 8 ) );
      System.out.println( "    Calling ius.getWeight(): expecting string and 175.0 out, got " + ius.getWeight() );
   }

}
