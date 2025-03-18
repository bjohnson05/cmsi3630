###
# filename: BinaryTree.py
# purpose:  binary tree simulation
# author:   Dr. Johnson
# date:     2023-02-24
###

from BinaryTreeNode import BinaryTreeNode

def press_return():
   input( "\n\n        [press 'enter' to see the result]... <=" );

def visit( current_node ):
      print( "(", current_node.get_data(), ")", end="" )
   
def pre_order_printer( current_node ):
   # You fill this in

def post_order_printer( current_node ):
   # You fill this in

def in_order_printer( current_node ):
   # You fill this in

def main():
   root = BinaryTreeNode( 0 );
   root.add_child( 1, "L" );
   root.add_child( 2, "R" );
   one = root.get_child( "L" );
   two = root.get_child( "R" );
   one.add_child( 3, "L" );
   one.add_child( 4, "R" );
   two.add_child( 5, "L" );
   two.add_child( 6, "R" );
   six = two.get_child( "R" );
   six.add_child( 7, "L" );
   six.add_child( 8, "R" );
   print( "one left: ", one.get_child("L").get_data() )

   print( "\n\n  ==== the tree looks like this [sorta]: \n\n" );
   print( "                  (", root.get_data(), ")" );
   print( "                   / \\" );
   print( "                  /   \\" );
   print( "                 /     \\" );
   print( "                /       \\" );
   print( "               /         \\" );
   print( "              /           \\" );
   print( "             /             \\" );
   print( "          (", one.get_data(), ")           (", two.get_data(), ")" );
   print( "           / \\             / \\" );
   print( "          /   \\           /   \\" );
   print( "         /     \\         /     \\" );
   print( "        /       \\       /       \\" );
   print( "     (", one.get_child("L").get_data(), ")", end="" )
   print( "     (", one.get_child("R").get_data(), ")", end="" )
   print( " (", two.get_child("L").get_data(), ")", end="" )
   print( "     (", two.get_child("R").get_data(), ")" );
   print( "                                / \\" );
   print( "                               /   \\" );
   print( "                            (", six.get_child("L").get_data(), ")", end="" )
   print( " (", six.get_child("R").get_data(), ")" );

   press_return()
   print( "\n\n   performing a pre_order_print....", end="" );
   pre_order_printer( root )
   press_return()
   print( "\n\n   performing a post_order_print....", end="" );
   post_order_printer( root )
   press_return()
   print( "\n\n   performing an in_order_print....", end="" );
   in_order_printer( root )
   print( "\n" )
main()
