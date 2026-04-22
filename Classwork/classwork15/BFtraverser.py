###
# filename: DFtraverser.py
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
      self.queuesize = 0
      self.printOrder = []

  # method to insert a vertex onto the stack
   def insert( self, vertex ):
      self.queue.append( vertex )
      self.queuesize += 1

  # method to remove a vertex off the queue
   def remove( self ):
      self.queuesize -= 1
      return self.queue.pop( 0 )

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
  #   note this is naturally iterative, since it's based on
  #   a queue.  When the queue is empty, stop
   def bft( self, graph, vLetter ):
      vertex = graph.vList[graph.getIndex( vLetter )]
      vertex.visit()
      self.insert( vertex )
      self.printOrder.append( vertex.displayMe() )
      while self.queuesize > 0:
         current = self.remove()
         if( len( current.adjacent ) != 0 ):
            for i in current.adjacent:
               nextV = graph.vList[ graph.getIndex( i ) ]
               if not nextV.isVisited():
                  nextV.visit()
                  self.insert( nextV )
                  self.printOrder.append( nextV.displayMe() )


###
#  Test area to check out all the Depth-First methods;
#     done by performing a DFT so it uses all the methods
###
print( "\n\n   Running BFtraverser tests." )
print( "   ==========================" )
print( "   Creating new graph for vertices 'A' through 'I'..." )
brdth = BFtraverser( 9 )
brdth.graph.printGraph()

print( "   Inserting nine vertices..." )
brdth.graph.insertVertex( 'A' )
brdth.graph.insertVertex( 'B' )
brdth.graph.insertVertex( 'C' )
brdth.graph.insertVertex( 'D' )
brdth.graph.insertVertex( 'E' )
brdth.graph.insertVertex( 'F' )
brdth.graph.insertVertex( 'G' )
brdth.graph.insertVertex( 'H' )
brdth.graph.insertVertex( 'I' )
brdth.graph.printGraph()

print( "\n   Connecting vertices per sample graph from class..." )
brdth.graph.connect( 'A', 'B' )
brdth.graph.connect( 'A', 'C' )
brdth.graph.connect( 'A', 'D' )
brdth.graph.connect( 'A', 'E' )
brdth.graph.connect( 'B', 'F' )
brdth.graph.connect( 'F', 'H' )
brdth.graph.connect( 'D', 'G' )
brdth.graph.connect( 'G', 'I' )
brdth.graph.printGraph()

print( "\n   Calling BFT routine, starting at vertex 'A'..." )
brdth.bft( brdth.graph, 'A' )
print( "   Result of BFT, order is:\n     ", brdth.printOrder )

print( "\n\n   Recreating same graph for vertices 'A' through 'I'..." )
brdth = BFtraverser( 9 )
print( "   Inserting nine vertices again as before..." )
brdth.graph.insertVertex( 'A' )
brdth.graph.insertVertex( 'B' )
brdth.graph.insertVertex( 'C' )
brdth.graph.insertVertex( 'D' )
brdth.graph.insertVertex( 'E' )
brdth.graph.insertVertex( 'F' )
brdth.graph.insertVertex( 'G' )
brdth.graph.insertVertex( 'H' )
brdth.graph.insertVertex( 'I' )
brdth.graph.printGraph()

print( "\n   Connecting vertices per sample graph as before..." )
brdth.graph.connect( 'A', 'B' )
brdth.graph.connect( 'A', 'C' )
brdth.graph.connect( 'A', 'D' )
brdth.graph.connect( 'A', 'E' )
brdth.graph.connect( 'B', 'F' )
brdth.graph.connect( 'F', 'H' )
brdth.graph.connect( 'D', 'G' )
brdth.graph.connect( 'G', 'I' )
brdth.graph.printGraph()

print( "\n   Calling BFT routine, starting at vertex 'G'..." )
brdth.bft( brdth.graph, 'G' )
print( "   Result of BFT, order is:\n     ", brdth.printOrder )

print( "\n\n   Recreating different graph for vertices 'A' through 'L'..." )
print( "   This is the graph from the in-class exercise...")
brdth = BFtraverser( 12 )
print( "   Inserting nine vertices again as before..." )
brdth.graph.insertVertex( 'A' )
brdth.graph.insertVertex( 'B' )
brdth.graph.insertVertex( 'C' )
brdth.graph.insertVertex( 'D' )
brdth.graph.insertVertex( 'E' )
brdth.graph.insertVertex( 'F' )
brdth.graph.insertVertex( 'G' )
brdth.graph.insertVertex( 'H' )
brdth.graph.insertVertex( 'I' )
brdth.graph.insertVertex( 'J' )
brdth.graph.insertVertex( 'K' )
brdth.graph.insertVertex( 'L' )
brdth.graph.printGraph()

print( "\n   Connecting vertices per new sample graph..." )
brdth.graph.connect( 'A', 'B' )
brdth.graph.connect( 'A', 'C' )
brdth.graph.connect( 'A', 'D' )
brdth.graph.connect( 'C', 'F' )
brdth.graph.connect( 'C', 'G' )
brdth.graph.connect( 'D', 'E' )
brdth.graph.connect( 'D', 'H' )
brdth.graph.connect( 'F', 'I' )
brdth.graph.connect( 'G', 'J' )
brdth.graph.connect( 'J', 'H' )
brdth.graph.connect( 'J', 'L' )
brdth.graph.connect( 'H', 'E' )
brdth.graph.connect( 'H', 'K' )
brdth.graph.printGraph()

print( "\n   Calling BFT routine, starting at vertex 'D'..." )
brdth.bft( brdth.graph, 'D' )
print( "   Result of BFT, order is:\n     ", brdth.printOrder )

print( "\n\n   BFT tests complete." )
print( "   ===================" )
