/* ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 *  HighArrayApp.java
 *  Array demonstration class
 * ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ */

class HighArrayApp {

   public static void main( String[] args ) {

      int maxSize = 100;      // arbitrarily set max array size
      HighArray arr;          // reference to array

      arr = new HighArray( maxSize );    // create the array
      arr.insert( 77 );                  // insert 10 items
      arr.insert( 99 );
      arr.insert( 44 );
      arr.insert( 55 );
      arr.insert( 22 );
      arr.insert( 88 );
      arr.insert( 11 );
      arr.insert( 00 );
      arr.insert( 66 );
      arr.insert( 33 );
      arr.display();                   // display items
      int searchKey = 35;              // search for item
      if( arr.find( searchKey ) ) {
         System.out.println( "Found " + searchKey );
      } else {
         System.out.println( "Did not find " + searchKey );
      }
      searchKey = 77;              // search for item
      if( arr.find( searchKey ) ) {
         System.out.println( "Found " + searchKey );
      } else {
         System.out.println( "Did not find " + searchKey );
      }
      arr.delete( 00 );          // delete 3 items
      arr.delete( 55 );
      arr.delete( 99 );
      arr.display();             // display items again
      System.out.println( "Current max value is: " + arr.getMax() );    // should return 88
      arr.insert( 99 );
      arr.display();
      System.out.println( "Current max value is: " + arr.getMax() );    // should return 99
      arr.delete( 99 );
      arr.delete( 88 );
      arr.display();
      System.out.println( "Current max value is: " + arr.getMax() );    // should return 77
      arr.insert( 222 );
      arr.insert( 111 );
      arr.display();
      System.out.println( "Current max value is: " + arr.getMax() );    // should return 222
      arr.delete( 222 );
      arr.display();
      System.out.println( "Current max value is: " + arr.getMax() );    // should return 111
      arr.insert( 11 );
      arr.insert( 00 );
      arr.insert( 66 );
      arr.insert( 33 );
      arr.display();
      System.out.println( "removing dupes");
      arr.noDups();
      arr.display();
      arr.insert( 33 );
      arr.insert( 33 );
      arr.insert( 33 );
      arr.insert( 33 );
      arr.insert( 33 );
      arr.display();
      System.out.println( "removing dupes");
      arr.noDups();
      arr.display();
   }
}
