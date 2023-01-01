/**
 *  filename: InterfaceUser.java
 *  purpose: to show how interfaces can be used to simulate polymorphism in Java
 *    which other languages [like C++ for example] allow directly
 *  author:  Dr. Johnson
 *  date:  2020-08-17
 */

public class InterfaceUser implements InterfaceDemo, InterfaceB {

   public InterfaceUser() {
      System.out.println( "\n   InterfaceUser object created..." );
   }

  /**
   *  these three methods are the IMPLEMENTATIONS of the methods defined in the
   *     InterfaceDemo interface
   */
   public double addThree( double in ) {
      return in + 3.0;
   }

   public String sayHi( String name ) {
      System.out.println( "      In InterfaceUser, hello " + name + " [this will appear first]" );
      return "done";
   }

   public boolean isTrue( boolean b ) {
      return b;
   }

  /**
   *  these three methods are the IMPLEMENTATIONS of the methods defined in the
   *     InterfaceB interface
   */
   public double divideBySeven( double in ) {
      return in / 7.0;
   }

   public char getFirstChar( String s ) {
      return s.charAt( 0 );
   }

   public void sayMyName( String name ) {
      System.out.println( "      In InterfaceUser, howdy-do " + name );
   }

  /**
   *  this is the main that calls the implementations
   */
   public static void main( String [] args ) {

      InterfaceUser iu = new InterfaceUser();
      System.out.println( "    Calling iu.addThree(7): expecting 10.0, got " + iu.addThree( 7.0 ) );
      System.out.println( "    Calling iu.sayHi(\"bozo\"): expecting \"done\", got " + iu.sayHi( "bozo" ) );
      System.out.println( "    Calling iu.isTrue( 0 == 0 ): expecting true, got : " + iu.isTrue( 0 == 0 ) );
      System.out.println( "    Calling iu.divideBySeven(123456.789): expecting 17,636.68414, got " + iu.divideBySeven( 123456.789 ) );
      System.out.println( "    Calling iu.getFirstChar(\"test string\"): expecting \"t\", got " + iu.getFirstChar( "test string" ) );
      System.out.println( "    Calling iu.sayMyName( \"Winifred\" ): expecting printed message : " );
      iu.sayMyName( "Winifred" );

   }

}
