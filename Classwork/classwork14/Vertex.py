###
# filename: Vertex.py
# purpose: demonstration of graph and depth first search
# author:   Dr. Johnson
# date:     2023-04-09
###

class Vertex:

   def __init__( self, value ):
      self.data = value       # letter value of vertex
      self.visited = False    # 'True' when visited
      self.adjacent = []      # list of vertex objects

   def visit( self ):
      self.visited = True
      return

   def getValue( self ):
      return self.data

   def isVisited( self ):
      return self.visited

   def setAdjacent( self, vertex2 ):
      self.adjacent.append( vertex2 )
      return

   def getAdjacent( self, which ):
      return self.adjacent[which]

   def allAdjacentVisited( self ):
      for i in self.adjacent:
         if not i.isVisited():
            return False
      return True

   def displayMe( self ):
      return str( "[" + self.data + "|" + str(self.visited) + "]" )

   def getMe( self ):
      v = vertex( self, self.data )
      v.visited= self.isVisited
      v.adjacent = self.adjacent.copy()
      return v

   def printAdjacencyList( self ):
      for i in range( len( self.adjacent ) ):
         print( "   i:", i, ", adjacent[", i, "]:", self.adjacent[i] )


print( "\n\n   Running vertex method tests." )
print( "   ============================\n" )
v1 = Vertex( 'A' )
v2 = Vertex( 'B' )
v3 = Vertex( 'C' )
print( "   v1: ", v1 )
print( "   v2: ", v2 )
print( "   v3: ", v3 )
print( "   v1 data:", v1.getValue() )
print( "   v2 data:", v2.getValue() )
print( "   v3 data:", v3.getValue() )
print( "   Before visiting...." )
print( "   v1 visited:", v1.isVisited() )
print( "   v2 visited:", v2.isVisited() )
print( "   v3 visited:", v3.isVisited() )
v1.visit()
v2.visit()
print( "   After visiting...." )
print( "   v1 isVisited:", v1.isVisited() )
print( "   v2 isVisited:", v2.isVisited() )
print( "   v3 isVisited:", v3.isVisited() )
print( "   Setting adjacency to v1" )
v1.setAdjacent( v2 )
v1.setAdjacent( v3 )
print( "   v1 adjacency list: ", v1.adjacent )
print( "   v1 is adjacent to:", v1.getAdjacent( 0 ).getValue() )
print( "   v1 is adjacent to:", v1.getAdjacent( 1 ).getValue() )
print( "   displaying v1: ", v1.displayMe() )
print( "   displaying v2 and v3: ", v2.displayMe(), v3.displayMe() )

print( "   v1 adjacency list: ", v1.adjacent )
v1.printAdjacencyList()
print( "   v1 all adjacent vertices visited: ", v1.allAdjacentVisited() )
v3.visit()
print( "   v1 all adjacent vertices visited: ", v1.allAdjacentVisited() )

print( "\n\n   Vertex tests complete." )
print( "   ======================" )
