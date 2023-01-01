/**
 *  File name: BinaryTree.java
 *  Purpose: Demonstrates a binary tree
 *  @author: B.J. Johnson
 *  @date: 2019-10-23
 *  @date: 2020-08-05: modified to use "Traversal" class with static methods
 */

import java.util.Scanner;

public class BinaryTree {

   public static void pressReturn() {
      System.out.print( "        [press 'enter' to see the result]... <=" );
      Scanner myInput = new Scanner( System.in );
      myInput.nextLine();
   }

   public static void main( String[] args ) {
      BinaryTreeNode root = new BinaryTreeNode( 0 );
      root.add( 1, "L" );
      root.add( 2, "R" );
      BinaryTreeNode one = root.getChild( "L" );
      BinaryTreeNode two = root.getChild( "R" );
      one.add( 3, "L" );
      one.add( 4, "R" );
      two.add( 5, "L" );
      two.add( 6, "R" );
      BinaryTreeNode six = two.getChild( "R" );
      six.add( 7, "L" );
      six.add( 8, "R" );

      System.out.println( "\n\n  ==== the tree looks like this [sorta]: \n\n" );
      System.out.println( "                   (0)" );
      System.out.println( "                   / \\" );
      System.out.println( "                  /   \\" );
      System.out.println( "                 /     \\" );
      System.out.println( "                /       \\" );
      System.out.println( "              (1)       (2)" );
      System.out.println( "              / \\       / \\" );
      System.out.println( "             /   \\     /   \\" );
      System.out.println( "           (3)   (4) (5)   (6)" );
      System.out.println( "                           / \\" );
      System.out.println( "                          /   \\" );
      System.out.println( "                        (7)   (8)" );

      System.out.println( "\n\n   Now doing a 'pre-order' traversal...\n" );
      pressReturn();
      System.out.print( "        " );
      Traversals.preOrderPrinter( root );
      System.out.println( "\n\n   Now doing a 'post-order' traversal...\n" );
      pressReturn();
      System.out.print( "        " );
      Traversals.postOrderPrinter( root );
      System.out.println( "\n\n   Now doing an 'in-order' traversal...\n" );
      pressReturn();
      System.out.print( "        " );
      Traversals.inOrderPrinter( root );
      System.out.print( "\n\n\n" );
   }
}
