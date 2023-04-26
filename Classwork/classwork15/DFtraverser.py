###
# filename: DFtraverser.py
# purpose: demonstration of graph and depth first traversal
# author:   Dr. Johnson
# date:     2023-04-09
###

from TheGraph import TheGraph

class DFtraverser():

  # constructor
   def __init__( self, size ):
      self.graph = TheGraph( size )
      self.stack = []
      self.stacksize = 0
      self.printOrder = []

  # method to push a vertex onto the stack
   def push( self, vertex ):
      self.stack.append( vertex )
      self.stacksize += 1

  # method to pop a vertex off the stack
   def pop( self ):
      self.stacksize -= 1
      self.stack.pop(self.stacksize)
      return

  # helper method to print the stack contents
   def printStack( self ):
      print( "   ", end = "" )
      if( len( self.stack ) > 0 ):
         for i in self.stack:
            print( i.displayMe(), end = "" )
            print()
      else:
         print( "   Stack is empty." )

  # depth-first traversal method [recursive]
  #   note there is a lot of functionality that happens PRIOR
  #   to the recursion.  This includes the base case, but also
  #   includes the stack manipulation
   def dft( self, graph, vLetter ):
      vertex = graph.vList[graph.getIndex( vLetter )]
      if not vertex.isVisited():
         vertex.visit()
      self.push( vertex )
      self.printOrder.append( vertex.displayMe() )
      if( len( vertex.adjacent ) != 0 ):
         for i in vertex.adjacent:
            next = graph.vList[graph.getIndex( i )]
            if not next.isVisited():
               self.dft( graph, next.getValue() )
         self.pop()
         return

###
#  Test area to check out all the Depth-First methods;
#     done by performing a DFT so it uses all the methods
###
print( "\n\n   Running DFtraverser tests." )
print( "   ==========================" )
print( "   Creating new graph for vertices 'A' through 'I'..." )
dpth = DFtraverser( 9 )
dpth.graph.printGraph()

print( "   Inserting nine vertices..." )
dpth.graph.insert( 'A' )
dpth.graph.insert( 'B' )
dpth.graph.insert( 'C' )
dpth.graph.insert( 'D' )
dpth.graph.insert( 'E' )
dpth.graph.insert( 'F' )
dpth.graph.insert( 'G' )
dpth.graph.insert( 'H' )
dpth.graph.insert( 'I' )
dpth.graph.printGraph()

print( "\n   Connecting vertices per sample graph from class..." )
dpth.graph.connect( 'A', 'B' )
dpth.graph.connect( 'A', 'C' )
dpth.graph.connect( 'A', 'D' )
dpth.graph.connect( 'A', 'E' )
dpth.graph.connect( 'B', 'F' )
dpth.graph.connect( 'F', 'H' )
dpth.graph.connect( 'D', 'G' )
dpth.graph.connect( 'G', 'I' )
dpth.graph.printGraph()

print( "\n   Calling DFT routine, starting at vertex 'A'..." )
dpth.dft( dpth.graph, 'A' )
print( "   Result of DFT, order is:\n     ", dpth.printOrder )

print( "\n\n   Recreating same graph for vertices 'A' through 'I'..." )
dpth = DFtraverser( 9 )
print( "   Inserting nine vertices again as before..." )
dpth.graph.insert( 'A' )
dpth.graph.insert( 'B' )
dpth.graph.insert( 'C' )
dpth.graph.insert( 'D' )
dpth.graph.insert( 'E' )
dpth.graph.insert( 'F' )
dpth.graph.insert( 'G' )
dpth.graph.insert( 'H' )
dpth.graph.insert( 'I' )
dpth.graph.printGraph()

print( "\n   Connecting vertices per sample graph as before..." )
dpth.graph.connect( 'A', 'B' )
dpth.graph.connect( 'A', 'C' )
dpth.graph.connect( 'A', 'D' )
dpth.graph.connect( 'A', 'E' )
dpth.graph.connect( 'B', 'F' )
dpth.graph.connect( 'F', 'H' )
dpth.graph.connect( 'D', 'G' )
dpth.graph.connect( 'G', 'I' )
dpth.graph.printGraph()

print( "\n   Calling DFT routine, starting at vertex 'G'..." )
dpth.dft( dpth.graph, 'G' )
print( "   Result of DFT, order is:\n     ", dpth.printOrder )

print( "\n\n   DFT tests complete." )
print( "   ===================" )
