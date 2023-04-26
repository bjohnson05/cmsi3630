###
# filename: BFtraverser.py
# purpose: demonstration of graph and depth first traversal
# author:   Dr. Johnson
# date:     2023-04-09
###

from TheGraph import TheGraph

class BFtraverser():

  # constructor
   def __init__( self, size ):
      self.graph = TheGraph( size )
      self.queue = []
      self.queueSize = 0
      self.printOrder = []

  # method to insert a vertex into the queue
   def insert( self, vertex ):
      self.queue.append( vertex )
      self.queueSize += 1

  # method to remove a vertex from the queue
   def remove( self ):
      self.queueSize -= 1
      self.queue = self.queue[ 1: ]
      return

  # helper method to print the queue contents
   def printQueue( self ):
      print( "   ", end = "" )
      if( len( self.queue ) > 0 ):
         for i in self.queue:
            print( i.displayMe(), end = "" )
            print()
      else:
         print( "   Queue is empty." )

  # breadth-first traversal method [recursive]
  #   note there is a lot of functionality that happens PRIOR
  #   to the recursion.  This includes the base case, but also
  #   includes the queue manipulation
   def bft( self, graph, vLetter ):
      vertex = graph.vList[graph.getIndex( vLetter )]
      if( len( self.queue ) == 0 ):
         self.insert( vertex )
      vertex.visit()
      self.printOrder.append( vertex.displayMe() )
      if( len( vertex.adjacent ) != 0 ):
         for i in vertex.adjacent:
            next = graph.vList[graph.getIndex( i )]
            if not next.isVisited():
               self.insert( next )
      self.remove()
      if( len( self.queue ) != 0 ):
         self.bft( graph, self.queue[0].getValue() )
      return

###
#  Test area to check out all the Depth-First methods;
#     done by performing a BFT so it uses all the methods
###
print( "\n\n   Running BFtraverser tests." )
print( "   ==========================" )
print( "   Creating graph for vertices 'A' through 'I'..." )
brdth = BFtraverser( 9 )
brdth.graph.printGraph()

print( "   Inserting nine vertices..." )
brdth.graph.insert( 'A' )
brdth.graph.insert( 'B' )
brdth.graph.insert( 'C' )
brdth.graph.insert( 'D' )
brdth.graph.insert( 'E' )
brdth.graph.insert( 'F' )
brdth.graph.insert( 'G' )
brdth.graph.insert( 'H' )
brdth.graph.insert( 'I' )
brdth.graph.printGraph()

print( "\n   Connecting vertices per sample graph..." )
brdth.graph.connect( 'A', 'B' )
brdth.graph.connect( 'A', 'C' )
brdth.graph.connect( 'A', 'D' )
brdth.graph.connect( 'A', 'E' )
brdth.graph.connect( 'B', 'F' )
brdth.graph.connect( 'F', 'H' )
brdth.graph.connect( 'D', 'G' )
brdth.graph.connect( 'G', 'I' )
brdth.graph.printGraph()

print( "\n   Calling BFS routine, starting at vertex 'A'..." )
brdth.bft( brdth.graph, 'A' )
print( "   Result of BFS, order is:\n     ", brdth.printOrder )

print( "\n\n   Recreating graph for vertices 'A' through 'I'..." )
brdth = BFtraverser( 9 )
print( "   Inserting nine vertices..." )
brdth.graph.insert( 'A' )
brdth.graph.insert( 'B' )
brdth.graph.insert( 'C' )
brdth.graph.insert( 'D' )
brdth.graph.insert( 'E' )
brdth.graph.insert( 'F' )
brdth.graph.insert( 'G' )
brdth.graph.insert( 'H' )
brdth.graph.insert( 'I' )
brdth.graph.printGraph()

print( "\n   Connecting vertices per sample graph..." )
brdth.graph.connect( 'A', 'B' )
brdth.graph.connect( 'A', 'C' )
brdth.graph.connect( 'A', 'D' )
brdth.graph.connect( 'A', 'E' )
brdth.graph.connect( 'B', 'F' )
brdth.graph.connect( 'F', 'H' )
brdth.graph.connect( 'D', 'G' )
brdth.graph.connect( 'G', 'I' )
brdth.graph.printGraph()
print( "\n   Calling BFS routine, starting at vertex 'G'..." )
brdth.bft( brdth.graph, 'G' )
print( "   Result of BFS, order is:\n     ", brdth.printOrder )
