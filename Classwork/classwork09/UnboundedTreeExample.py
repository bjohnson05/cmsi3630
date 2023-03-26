###
# filename: UnboundedTreeExample.py
# purpose:  unbounded tree example demo
# author:   Dr. Johnson
# date:     2023-02-24
###

from UnboundedTreeNode import UnboundedTreeNode

def main():

   rootValue = 23
   rootFirstChildIndex = 0
   rootThirdChildIndex = 2

   root = UnboundedTreeNode( rootValue )
   root.add_child( 2 )      # root's first child at index zero
   root.add_child( 3 )      #        second child at index one
   root.add_child( 4 )      #        third child at index two

   it = root.get_child( rootFirstChildIndex )
   it.add_child( 5 )        # root's first child's first child
   it.add_child( 6 )

   it2 = root.get_child( rootThirdChildIndex )
   it2.add_child( 7 )       # root's second child's first child
   it2.add_child( 8 )
   it2.add_child( 9 )
   it2.add_child( 10 )
   it2.add_child( 11 )
   it2.add_child( 12 )
   it2.add_child( 13 )
   it2.add_child( 14 )

   print( "\n Children of root: ", end="" )
   for i in range( root.num_kids ):
      print( "[" + root.get_child( i ).get_value() + "]", end="" )
   print()

   print( "\n Children of root's first child: ", end="" )
   for i in range( it.num_kids ):
      print( "[" + it.get_child( i ).get_value() + "]", end="" )
   print()

   print( "\n Children of root's third child: ", end="" )
   for i in range( it2.num_kids ):
      print( "[" + it2.get_child( i ).get_value() + "]", end="" )
   print()

   it3 = it2.get_child( 7 )
   it3.add_child( 15 )
   it3.add_child( 16 )
   it3.add_child( 17 )
   it3.add_child( 18 )

   print( "\n Children of root's third child's last child: ", end="" )
   for i in range( it3.num_kids ):
      print( "[" + it3.get_child( i ).get_value() + "]", end="" )
   print()

   print( "\n Proving the 'daisy-chain' effect" )
   print( "  Using multiple 'get_child' calls from root to get last leaf")
   print( " root's last great-grandchild: ", end="" )
   print( root.get_child( rootThirdChildIndex ).get_child(7).get_child(3).get_value() )
   print("\n\n")

main()
