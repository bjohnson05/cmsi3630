###
# filename: graph.py
# purpose: Provide a Graph class for the depth first search demo
# author:   Dr. Johnson
# date:     2023-04-07
###

class Graph:

   DEBUG = True

  # Constructor for the graph; this just declares the lists, then
  #   simply initializes the adjacency matrix to all zeroes and the
  #   visited list to all False
   def __init__( self, numVertices ):
      self.adjaMatrix = [[0] * numVertices] * numVertices
      self.visited    = [False] * numVertices

      if self.DEBUG:
         print( self.visited )
         print( self.adjaMatrix )

  # Calculate a vertex's index based on its letter name (ASCII)
   def convertToIndex( self, vertexName ):
      return ord( vertexName ) - ord( 'A' )

  # Mark two vertexs as connected.  This is done by putting a "1" in
  #  each of the cells in the adjacency matrix for the two connected vertexs
   def link( self, vertIndex1, vertIndex2 ):
      self.adjaMatrix[vertIndex1][vertIndex2] = 1;
      self.adjaMatrix[vertIndex2][vertIndex1] = 1;

  # Make a link between two vertexs by calling the "link()" method with
  #  their converted indices; note that we have to FIND each vertex's index
   def linkTwoVertices( self, vertexOne, vertexTwo ):
      self.link( self.convertToIndex(vertexOne), self.convertToIndex(vertexTwo) )

  # Check if two vertices are connected
   def areTwoVertexsConnected( self, vertexOne, vertexTwo ):
      return( self.adjaMatrix[self.convertToIndex(vertexOne)] \
                             [self.convertToIndex(vertexTwo)] == 1 )

  # Mark a vertex as having been visited
   def visit( self, vertex ):
      self.visited[self.convertToIndex( vertex )] = True

  # Check if this vertex has been visited already
   def wasVisited( self, vertex ):
      index = self.convertToIndex( vertex )
      return( self.visited[index] )

def main():
   g = Graph( 9 )

main()
