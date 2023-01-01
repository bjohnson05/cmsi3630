/**
 *  File name: BinaryTreeNode.java
 *  Purpose: Demonstrates a binary tree
 *  @author: B.J. Johnson
 *  @date: 2019-10-23
 */

public class BinaryTreeNode {

   public  int data;
   private BinaryTreeNode left;
   private BinaryTreeNode right;

   BinaryTreeNode( int d ) {
       data = d;
       left = null;
       right = null;
   }

   public void add( int s, String child ) {
      child = child.toUpperCase();
      if( child.equals( "L" ) ) {
         left = new BinaryTreeNode( s );
      } else if( child.equals( "R" ) ) {
         right = new BinaryTreeNode( s );
      } else {
         throw new IllegalArgumentException();
      }
   }

   public BinaryTreeNode getChild( String child ) {
      child = child.toUpperCase();
      if( child.equals("L") || child.equals("R") ) {
         return (child.equals("L") ? left : right);
      } else {
         throw new IllegalArgumentException();
      }
   }

   public int getData() {
       return data;
   }
}
