/**
 * filename: BinaryTree.java
 * purpose : demonstrates tree functions
 * @author : B.J. Johnson from Lafore book
 * @date   : 2018-11-26
 * @version: 1.0.0
 */

import java.util.Stack;                      // for Stack class

/**
 * class for the Tree Node
 */
class BinaryTreeNode {
   public int              iData;         // data item (key)
   public double           dData;         // data item
   public BinaryTreeNode   leftChild;     // this node's left child
   public BinaryTreeNode   rightChild;    // this node's right child

  /**
   * Constructor
   */
   public BinaryTreeNode( int key, double value ) {
      iData = key;
      dData = value;
      leftChild = null;
      rightChild = null;
   }

  /**
   * Method to display this node
   */
   public void displayNode() {            // display ourself
      System.out.print( '{' );
      System.out.print( iData );
      System.out.print( ", " );
      System.out.print( dData );
      System.out.print( "} " );
   }
}


public class BinaryTree {

   private BinaryTreeNode root;           // first BinaryTreeNode of tree

  /**
   * Constructor
   */
   public BinaryTree() {
      root = null;
   }

   /**
    * Method to find a BinaryTreeNode in the tree
    * @param key integer value we seek
    * @return BinaryTreeNode value that is found or null if not there
    */
   public BinaryTreeNode find( int key ) {
      BinaryTreeNode current = root;
      while( current.iData != key ) {
         if( key < current.iData ) {
            current = current.leftChild;
         } else {
            current = current.rightChild;
         }
         if( current == null ) {
            return null;
         }
      }
      return current;
   }

  /**
   * Method to insert a BinaryTreeNode into the tree
   * NOTE: assumes non-empty list
   * @param id integer value of the key of the node
   * @param dd double value of the data of the node
   */
   public void insert( int id, double dd ) {

      BinaryTreeNode newNode = new BinaryTreeNode( id, dd );

      if( root == null ) {
         root = newNode;
      } else {
         BinaryTreeNode current = root;
         BinaryTreeNode parent;
         while( true ) {
            parent = current;
            if( id < current.iData ) {          // go left?
               current = current.leftChild;
               if( current == null ) {          // if end of the line,
                  parent.leftChild = newNode;
                  return;
               }
            } else {                            // ...or go right?
               current = current.rightChild;
               if( current == null ) { // insert on right
                  parent.rightChild = newNode;
                  return;
               }
            }
         }
      }
   }

  /**
   * Method to delete a BinaryTreeNode from the tree
   * NOTE: assumes non-empty list
   * @param id integer value of the key of the node
   * @param dd double value of the data of the node
   */
   public boolean delete( int key ) {

      BinaryTreeNode current = root;
      BinaryTreeNode parent = root;
      boolean isLeftChild = true;

      while( current.iData != key ) {
         parent = current;
         if( key < current.iData ) {      // go left?
            isLeftChild = true;
            current = current.leftChild;
         } else {                         // or go right?
            isLeftChild = false;
            current = current.rightChild;
         }
         if( current == null ) {          // or if we're at the end of the line,
            return false;                 //  we didn't find the key!
         }
      }
     // we found the BinaryTreeNode to delete
     // if it has no children, simply delete it
      if( (current.leftChild == null) && (current.rightChild == null) ) {
         if(current == root) {            // if it's the root,
            root = null;                  //  then the tree is empty
         } else if( isLeftChild ) {
            parent.leftChild = null;      // disconnect
         } else {                         // from parent
            parent.rightChild = null;
         }
      } else if( current.rightChild == null ) {    // if no right child, replace with left subtree
         if( current == root ) {
            root = current.leftChild;
         } else if( isLeftChild ) {
            parent.leftChild = current.leftChild;
         } else {
            parent.rightChild = current.leftChild;
         }
      } else if( current.leftChild == null ) {     // if no left child, replace with right subtree
         if( current == root ) {
            root = current.rightChild;
         } else if( isLeftChild ) {
            parent.leftChild = current.rightChild;
         } else{
            parent.rightChild = current.rightChild;
         }
      } else {                                     // two children, so replace with inorder successor

         BinaryTreeNode successor = getSuccessor( current ); // get successor of BinaryTreeNode to delete (current) then
                                                   // connect parent of current to successor instead
         if( current == root ) {
            root = successor;
         } else if( isLeftChild ) {
            parent.leftChild = successor;
         } else {
            parent.rightChild = successor;
         }
         successor.leftChild = current.leftChild;// connect successor to current's left child
      }
      return true;            // success
   }

  /**
   * returns BinaryTreeNode with next-highest value after delNode
   * goes to right child, then right child's left descendents
   * @param delNode BinaryTreeNode to be deleted from the tree
   * @return BinaryTreeNode that is deleted
   */
   private BinaryTreeNode getSuccessor(BinaryTreeNode delNode) {
      BinaryTreeNode successorParent = delNode;
      BinaryTreeNode successor = delNode;
      BinaryTreeNode current = delNode.rightChild; // go to right child
      while(current != null) // until no more
      { // left children,
      successorParent = successor;
      successor = current;
      current = current.leftChild; // go to left child
      }
      // if successor not
      if(successor != delNode.rightChild) // right child,
      { // make connections
      successorParent.leftChild = successor.rightChild;
      successor.rightChild = delNode.rightChild;
      }
      return successor;
   }

  /**
   * Executes a traversal based on the type passed as argument
   * @param traverseType traversal type 1 [pre-], 2 [in-], or 3 [post-] order
   */
   public void traverse( int traverseType ) {
      switch( traverseType ) {
         case 1:  System.out.print( "\nPreorder traversal: " );
                  preOrder( root );
                  break;
         case 2:  System.out.print( "\nInorder traversal: " );
                  inOrder( root );
                  break;
         case 3:  System.out.print( "\nPostorder traversal: " );
                  postOrder( root );
                  break;
      }
      System.out.println();
   }

  /**
   * Executes a recursive pre-order traversal
   * @param localRoot BinaryTreeNode which is the local root of the sub-tree
   */
   private void preOrder( BinaryTreeNode localRoot) {
      if( localRoot != null ) {
         System.out.print( localRoot.iData + " " );
         preOrder( localRoot.leftChild );
         preOrder( localRoot.rightChild );
      }
   }

  /**
   * Executes a recursive in-order traversal
   * @param localRoot BinaryTreeNode which is the local root of the sub-tree
   */
   private void inOrder( BinaryTreeNode localRoot ) {
      if( localRoot != null ) {
         inOrder( localRoot.leftChild );
         System.out.print( localRoot.iData + " " );
         inOrder( localRoot.rightChild );
      }
   }

  /**
   * Executes a recursive post-order traversal
   * @param localRoot BinaryTreeNode which is the local root of the sub-tree
   */
   private void postOrder( BinaryTreeNode localRoot ) {
      if(localRoot != null) {
         postOrder( localRoot.leftChild );
         postOrder( localRoot.rightChild );
         System.out.print( localRoot.iData + " " );
      }
   }

  /**
   * displays the tree on the console window using a Stack
   */
   public void displayTree() {
      Stack <BinaryTreeNode>globalStack = new Stack<BinaryTreeNode>();
      globalStack.push( root );
      int nBlanks = 32;
      boolean isRowEmpty = false;
      System.out.println( "......................................................" );
      while( isRowEmpty == false ) {
         Stack <BinaryTreeNode>localStack = new Stack<BinaryTreeNode>();
         isRowEmpty = true;
         for( int j = 0; j < nBlanks; j++ ) {
            System.out.print(' ');
         }
         while( globalStack.isEmpty() == false ) {
            BinaryTreeNode temp = (BinaryTreeNode)globalStack.pop();
            if( temp != null ) {
               System.out.print( temp.iData );
               localStack.push( temp.leftChild );
               localStack.push( temp.rightChild );
               if( (temp.leftChild != null) || (temp.rightChild != null) ) {
                  isRowEmpty = false;
               }
            } else {
               System.out.print( "--" );
               localStack.push( null );
               localStack.push( null );
            }
            for( int j = 0; j < nBlanks * 2 - 2; j++ ) {
               System.out.print( ' ' );
            }
         }
         System.out.println();
         nBlanks /= 2;
         while( localStack.isEmpty() == false ) {
            globalStack.push( localStack.pop() );
         }
      }
         System.out.println( "......................................................" );
   }
}
