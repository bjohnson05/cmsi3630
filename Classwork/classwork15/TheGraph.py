###
# filename: TheGraph.py
# purpose: demonstration of graph and depth first search
# author:   Dr. Johnson
# date:     2023-04-09
###

from Vertex import Vertex

DEBUG = False

class TheGraph():

   def __init__( self, numVertices ):
      self.vCount = numVertices
      self.vList  = []
      if( DEBUG ):
         print( "   content vertex list:", self.vList )
         print( "   size of vertex list:", len( self.vList ) )

   def insert( self, vName ):
      v = Vertex( vName )
      self.vList.append( v )
      return

   def connect( self, vertex1, vertex2 ):
      index1 = self.getIndex( vertex1 )
      index2 = self.getIndex( vertex2 )
      self.vList[index1].setAdjacent( vertex2 )
      self.vList[index2].setAdjacent( vertex1 )
      return

   def printGraph( self ):
      print()
      for i in range( len( self.vList ) ):
         print( "   vList[", i, "]:", self.vList[i].getValue(), " adj:", self.vList[i].adjacent )
      return

   def getIndex( self, vName ):
      for i in range( len( self.vList ) ):
         if( self.vList[i].getValue() == vName ):
            return i
      return None


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
