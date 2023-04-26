###
# filename: TheGraph.py
# purpose: demonstration of graph and depth first search
# author:   Dr. Johnson
# date:     2023-04-09
###

from Vertex import Vertex

DEBUG = False

class TheGraph():

  # constructor
  #   note: also uses DEBUG
   def __init__( self, numVertices ):
      self.vCount = numVertices
      self.vList  = []
      if( DEBUG ):
         print( "   content vertex list:", self.vList )
         print( "   size of vertex list:", len( self.vList ) )

  # method to insert a vertex into the graph
  #   note: uses the NAME data for the vertex
   def insert( self, vName ):
      v = Vertex( vName )
      self.vList.append( v )
      return

  # method to connect two vertices
  #   [make them adjacent to each other]
   def connect( self, vertex1, vertex2 ):
      index1 = self.getIndex( vertex1 )
      index2 = self.getIndex( vertex2 )
      self.vList[index1].setAdjacent( vertex2 )
      self.vList[index2].setAdjacent( vertex1 )
      return

  # method to get the index into the vertex name list
  #   given its name data
  #   returns "None" if it's not there
   def getIndex( self, vName ):
      for i in range( len( self.vList ) ):
         if( self.vList[i].getValue() == vName ):
            return i
      return None

  # helper method that prints the graph's vertices along
  #   with each one's adjacency list
   def printGraph( self ):
      print()
      for i in range( len( self.vList ) ):
         print( "   vList[", i, "]:", self.vList[i].getValue(), " adj:", self.vList[i].adjacent )
      return

###
#  Test area to check out all the graph methods;
#     done by creating a graph so it uses all the methods
###
print( "\n\n   Running graph method tests." )
print( "   ===========================\n" )
print( "   Making new empty graph with room for 9 vertices" )
g = TheGraph( 9 )

print( "   Inserting vertices 'A' through 'I'..." )
g.insert( 'A' )
g.insert( 'B' )
g.insert( 'C' )
g.insert( 'D' )
g.insert( 'E' )
g.insert( 'F' )
g.insert( 'G' )
g.insert( 'H' )
g.insert( 'I' )
g.printGraph()

print( "\n   index of the F vertex: ", g.getIndex( 'F' ) )
print( "   value of the F vertex: ", g.vList[g.getIndex( 'F' )] )

print( "\n   joining vertices..." )
g.connect( 'A', 'B' )
g.connect( 'A', 'C' )
g.connect( 'A', 'D' )
g.connect( 'A', 'E' )
g.connect( 'B', 'F' )
g.connect( 'F', 'H' )
g.connect( 'D', 'G' )
g.connect( 'G', 'I' )
g.printGraph()

print( "   Testing getIndex() method" )
print( "   index of 'E' is: ", g.getIndex( 'E' ) )
print( "   index of 'Q' is: ", g.getIndex( 'Q' ) )

print( "\n\n   Graph tests complete." )
print( "   =====================" )
