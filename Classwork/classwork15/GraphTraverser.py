###
# filename: GraphTraverser.py
# purpose: demonstration of graph and depth/breadth first traversal
# author:   Dr. Johnson
# date:     2023-04-09
###

from TheGraph import TheGraph

class GraphTraverser():

  # constructor
   def __init__( self, size ):
      self.graph = TheGraph( size )
      self.stack = []
      self.queue = []
      self.size = 0
      self.printOrder = []

  # method to push a vertex onto the stack
   def push( self, vertex ):
      self.stack.append( vertex )
      self.size += 1
      return

  # method to pop a vertex off the stack
   def pop( self ):
      self.size -= 1
      self.stack.pop(self.size)
      return

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

  # method to insert a vertex onto the queue
   def queueInsert( self, vertex ):
      self.queue.append( vertex )
      self.size += 1
      return

  # method to remove a vertex off the queue
   def queueRemove( self ):
      self.size -= 1
      self.queue.pop( 0 )
      return

  # breadth-first traversal method [iterative]
  #   note there is a lot of functionality that happens PRIOR
  #   to the iteration.
   def bft( self, graph, vLetter ):
      vertex = graph.vList[graph.getIndex( vLetter )]
      if not vertex.isVisited():
         vertex.visit()
      if len( self.queue ) == 0:
         self.queueInsert( vertex )
         self.printOrder.append( vertex.displayMe() )
      if( len( vertex.adjacent ) != 0 ):
         for i in vertex.adjacent:
            next = graph.vList[graph.getIndex( i )]
            if not next.isVisited():
               self.queueInsert( next )
               self.printOrder.append( next.displayMe() )
         self.queueRemove()
         if len( self.queue ) != 0:
            next = self.queue[0]
         if not next.isVisited():
            self.bft( graph, next.getValue() )
      return


###
#  Test area to check out all the Depth-First methods;
#     done by performing a DFT so it uses all the methods
###
print( "\n\n   Running DFT traverser tests." )
print( "   ============================" )
print( "   Creating new graph for vertices 'A' through 'I'..." )
net = GraphTraverser( 9 )
net.graph.printGraph()

print( "   Inserting nine vertices..." )
net.graph.insertVertex( 'A' )
net.graph.insertVertex( 'B' )
net.graph.insertVertex( 'C' )
net.graph.insertVertex( 'D' )
net.graph.insertVertex( 'E' )
net.graph.insertVertex( 'F' )
net.graph.insertVertex( 'G' )
net.graph.insertVertex( 'H' )
net.graph.insertVertex( 'I' )
net.graph.printGraph()

print( "\n   Connecting vertices per sample graph from class..." )
net.graph.connect( 'A', 'B' )
net.graph.connect( 'A', 'C' )
net.graph.connect( 'A', 'D' )
net.graph.connect( 'A', 'E' )
net.graph.connect( 'B', 'F' )
net.graph.connect( 'F', 'H' )
net.graph.connect( 'D', 'G' )
net.graph.connect( 'G', 'I' )
net.graph.printGraph()

print( "\n   Calling DFT routine, starting at vertex 'A'..." )
net.dft( net.graph, 'A' )
print( "   Result of DFT, order is:\n     ", net.printOrder )

print( "\n\n   Recreating same graph for vertices 'A' through 'I'..." )
net = GraphTraverser( 9 )
print( "   Inserting nine vertices again as before..." )
net.graph.insertVertex( 'A' )
net.graph.insertVertex( 'B' )
net.graph.insertVertex( 'C' )
net.graph.insertVertex( 'D' )
net.graph.insertVertex( 'E' )
net.graph.insertVertex( 'F' )
net.graph.insertVertex( 'G' )
net.graph.insertVertex( 'H' )
net.graph.insertVertex( 'I' )
net.graph.printGraph()

print( "\n   Connecting vertices per sample graph as before..." )
net.graph.connect( 'A', 'B' )
net.graph.connect( 'A', 'C' )
net.graph.connect( 'A', 'D' )
net.graph.connect( 'A', 'E' )
net.graph.connect( 'B', 'F' )
net.graph.connect( 'F', 'H' )
net.graph.connect( 'D', 'G' )
net.graph.connect( 'G', 'I' )
net.graph.printGraph()

print( "\n   Calling DFT routine, starting at vertex 'G'..." )
net.dft( net.graph, 'G' )
print( "   Result of DFT, order is:\n     ", net.printOrder )

print( "\n\n   DFT tests complete." )
print( "   ===================" )

###
#  Test area to check out all the Depth-First methods;
#     done by performing a DFT so it uses all the methods
###
print( "\n\n   Running BFT traverser tests." )
print( "   ============================" )
print( "   Creating new graph for vertices 'A' through 'I'..." )
net = GraphTraverser( 9 )
net.graph.printGraph()

print( "   Inserting nine vertices..." )
net.graph.insertVertex( 'A' )
net.graph.insertVertex( 'B' )
net.graph.insertVertex( 'C' )
net.graph.insertVertex( 'D' )
net.graph.insertVertex( 'E' )
net.graph.insertVertex( 'F' )
net.graph.insertVertex( 'G' )
net.graph.insertVertex( 'H' )
net.graph.insertVertex( 'I' )
net.graph.printGraph()

print( "\n   Connecting vertices per sample graph from class..." )
net.graph.connect( 'A', 'B' )
net.graph.connect( 'A', 'C' )
net.graph.connect( 'A', 'D' )
net.graph.connect( 'A', 'E' )
net.graph.connect( 'B', 'F' )
net.graph.connect( 'F', 'H' )
net.graph.connect( 'D', 'G' )
net.graph.connect( 'G', 'I' )
net.graph.printGraph()

print( "\n   Calling BFT routine, starting at vertex 'A'..." )
net.bft( net.graph, 'A' )
print( "   Result of BFT, order is:\n     ", net.printOrder )

print( "   Creating new graph for vertices 'A' through 'I'..." )
net = GraphTraverser( 9 )
net.graph.printGraph()

print( "   Inserting nine vertices..." )
net.graph.insertVertex( 'A' )
net.graph.insertVertex( 'B' )
net.graph.insertVertex( 'C' )
net.graph.insertVertex( 'D' )
net.graph.insertVertex( 'E' )
net.graph.insertVertex( 'F' )
net.graph.insertVertex( 'G' )
net.graph.insertVertex( 'H' )
net.graph.insertVertex( 'I' )
net.graph.printGraph()

print( "\n   Connecting vertices per sample graph from class..." )
net.graph.connect( 'A', 'B' )
net.graph.connect( 'A', 'C' )
net.graph.connect( 'A', 'D' )
net.graph.connect( 'A', 'E' )
net.graph.connect( 'B', 'F' )
net.graph.connect( 'F', 'H' )
net.graph.connect( 'D', 'G' )
net.graph.connect( 'G', 'I' )
net.graph.printGraph()

print( "\n   Calling BFT routine, starting at vertex 'G'..." )
net.bft( net.graph, 'G' )
print( "   Result of BFT, order is:\n     ", net.printOrder )

print( "   Creating new graph for vertices 'A' through 'I'..." )
net = GraphTraverser( 9 )
net.graph.printGraph()

print( "   Inserting nine vertices..." )
net.graph.insertVertex( 'A' )
net.graph.insertVertex( 'B' )
net.graph.insertVertex( 'C' )
net.graph.insertVertex( 'D' )
net.graph.insertVertex( 'E' )
net.graph.insertVertex( 'F' )
net.graph.insertVertex( 'G' )
net.graph.insertVertex( 'H' )
net.graph.insertVertex( 'I' )
net.graph.printGraph()

print( "\n   Connecting vertices per sample graph from class..." )
net.graph.connect( 'A', 'B' )
net.graph.connect( 'A', 'C' )
net.graph.connect( 'A', 'D' )
net.graph.connect( 'A', 'E' )
net.graph.connect( 'B', 'F' )
net.graph.connect( 'F', 'H' )
net.graph.connect( 'D', 'G' )
net.graph.connect( 'G', 'I' )
net.graph.printGraph()

print( "\n   Calling BFT routine, starting at vertex 'H'..." )
net.bft( net.graph, 'H' )
print( "   Result of BFT, order is:\n     ", net.printOrder )
