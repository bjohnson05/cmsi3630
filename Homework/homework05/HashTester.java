public class HashTester {

   private static final int characterSize = 37;

   public static void main( String[] args ) {

      String key   = args[0].toLowerCase();
      int maxCount = key.length() - 1;
      int index    = 0;
      double j     = 0.0;
      System.out.println( "\n\n  Parameters:\n" +
                          "maxCount: " + maxCount + " index: " + index +
                          " j: " + j + " key.length(): " + key.length() );

      for( int i = maxCount; i >=0; i-- ) {
         int c = (key.codePointAt(i) - 32);
         System.out.println( "c: " + c );
         index += (c * Math.pow( 27.0, j )) % characterSize;
         j = j + 1.0;
      }

      System.out.println( "" );
      System.out.println( "    [Hash of " + key + " is: " + index + "]" );

   }
}
