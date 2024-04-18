/**
 * filename: BinaryTreeTester.java
 * purpose : demonstrates tree functions
 * @author : B.J. Johnson from Lafore book
 * @date   : 2018-11-28
 * @version: 1.0.0
 */

public class BinaryTreeTester {

   private static BinaryTree bt        = null;
   private static final int PRE_ORDER  = 1;
   private static final int IN_ORDER   = 2;
   private static final int POST_ORDER = 3;

   public static void main( String[] args ) {
         
      bt = new BinaryTree();
      bt.insert( 73, 0 );
      bt.insert( 50, 1 );
      bt.insert( 90, 2 );
      bt.insert( 30, 3 );
      bt.insert( 65, 4 );
      bt.insert( 82, 5 );
      bt.insert( 101, 6 );
      bt.displayTree();
      bt.traverse( IN_ORDER );

      bt.insert( 10, 7 );
      bt.insert( 42, 8 );
      bt.insert( 59, 9 );
      bt.insert( 69, 10 );
      bt.insert( 79, 11 );
      bt.insert( 87, 12 );
      bt.insert( 93, 13 );
      bt.insert( 110, 14 );
      bt.displayTree();
      bt.traverse( IN_ORDER );

   }
}