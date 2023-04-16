###
# filename: DFsearcher.py
# purpose: demonstration of graph and depth first search
# author:   Dr. Johnson
# date:     2023-04-09
###

from TheGraph import TheGraph

class DFsearcher():

   def __init__( self, size ):
      self.graph = TheGraph( size )
      self.stack = []
      self.stacksize = 0
      self.printOrder = []

   def push( self, vertex ):
      self.stack.append( vertex )
      self.stacksize += 1

   def pop( self ):
      self.stacksize -= 1
      self.stack.pop(self.stacksize)
      return

   def printStack( self ):
      print( "   ", end = "" )
      if( len( self.stack ) > 0 ):
         for i in self.stack:
            print( i.displayMe(), end = "" )
            print()

   def dfs( self, graph, vertex ):
      vertex = graph.vList[graph.getIndex( vertex )]
      if not vertex.isVisited():
         vertex.visit()
      self.push( vertex )
      self.printOrder.append( vertex.displayMe() )
      if( len( vertex.adjacent ) != 0 ):
         for i in vertex.adjacent:
            next = graph.vList[graph.getIndex( i )]
            if not next.isVisited():
               self.dfs( graph, next.getValue() )
         self.pop()
         return


print( "\n\n   Graph tests complete ~ running DFsearcher tests." )
print( "   ================================================" )
print( "   Creating graph for vertices 'A' through 'I'..." )
dpth = DFsearcher( 9 )
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

print( "\n   Connecting vertices per sample graph..." )
dpth.graph.connect( 'A', 'B' )
dpth.graph.connect( 'A', 'C' )
dpth.graph.connect( 'A', 'D' )
dpth.graph.connect( 'A', 'E' )
dpth.graph.connect( 'B', 'F' )
dpth.graph.connect( 'F', 'H' )
dpth.graph.connect( 'D', 'G' )
dpth.graph.connect( 'G', 'I' )
dpth.graph.printGraph()

print( "\n   Calling DFS routine..." )
dpth.dfs( dpth.graph, 'A' )
print( "   Result of DFS, order is:\n     ", dpth.printOrder )
