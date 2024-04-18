/*
 * File name: InOrderTraverser.java
 * Purpose  : demonstrates one way to do tree traversal in-order
 * @author  : B.J. Johnson
 * @date    : 2018-11-04
 * @version : 1.0.0
 * Revision history: 2018-11-19 Initial writing and release
 *
 * Description:  Write a method that does an in-order traverse of a tree.
 *                It should display all the items in the proper order.
 *                Remember that in-order means you visit the left sub-tree,
 *                then the current node, then the right sub-tree.
 */

public class InOrderTraverser extends BinaryTree {

   private BinaryTree myTree;

  /**
   * Constructor makes a tree with a root node
   *  so we can add to it
   */
   public InOrderTraverser( String data ) {
      myTree = new BinaryTree( data );
   }

  /**
   * Method to visit a node in the tree
   * @param n TreeNode to visit [print]
   */
   public void visitNode( TreeNode n ) {
      if( !n.visited ) {
         System.out.print( "[" + n.data + "]" );
         n.visited = true;
      }
   }

  /**
   * Main method to run the operation
   */
   public static void main( String[] args ) {

      InOrderTraverser iot = new InOrderTraverser( "H" );
      iot.myTree.root.addChild( "D", "L" );
      iot.myTree.root.addChild( "J", "R" );
      iot.myTree.root.displayTreeNode();

   }

}
