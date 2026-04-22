###
# filename: depthfirstsearcher.py
# purpose: Provide a class for a depth first search of a graph
# author:   Dr. Johnson
# date:     2023-04-07
#  Description:  This class performs a recursive depth-first search on a
#     graph that is constructed with a user-entered number of nodes.  The
#      graph is expected to be of the associated "graph" class.
#
#  Operation is recursive; at each level, all the vertices in the graph are
#  checked for connectivity with the current vertex.  The first vertex that
#  is connected is used as the root of the next recursion.  Vertices are
#  implemented as an adjacency matrix, using a 2-D python list of lists, in
#  a pretty standard method.
#
#  There is also a boolean array to keep track of which vertices have been
#  visited. A number of methods for performing the operation are also
#  available.  All of these items are part of the Graph.py class which is
#  associated.  This class actually creates and connects the graph to be
#  searched.  It performs all the initializations, then does the search and
#  lists the vertices as they become the root at each level of recursion.
#  It's pretty basic, but it shows the idea.
###

from graph import Graph

TEST_GRAPH_SIZE = 9
DEBUG = True

class DepthFirstSearcher:


   def __init__( self, vertexCount ):
      self.size = vertexCount
      self.output = []
      self.index = 0

   def dfs( self, theGraph, vertCurrent ):
     # mark the current vertex a visited and print its name
      theGraph.visit( vertCurrent )
      print( "   ** Visited ", vertCurrent )
      self.output.append( vertCurrent )
      self.index += 1
     # check to see what other vertices are connected and recurse
      for vertNext in range( ord('A'), (ord('A') + TEST_GRAPH_SIZE - 1) ):
         if( theGraph.areTwoVertexsConnected( vertCurrent, chr( vertNext ) ) ):
            if( not theGraph.wasVisited( chr( vertNext ) ) ):
               self.dfs( theGraph, chr( vertNext ) )   # <-- HERE'S THE RECURSION!!
      return



###
# MAIN
#  The main method declares a graph of 9 Vertexs, initializes them and their
#  connections, then performs a DFS on the graph just listing out the Vertexs
#  as they are visited.  It also shows the checks
###
def main():
  # Create a new graph wih 8 Vertexs, which will be named 'A' through 'I'
   theGraph = Graph( TEST_GRAPH_SIZE )

  # Create links between the Vertexs.
   theGraph.linkTwoVertices( 'A', 'B' );
   theGraph.linkTwoVertices( 'A', 'C' );
   theGraph.linkTwoVertices( 'A', 'D' );
   theGraph.linkTwoVertices( 'A', 'E' );
   theGraph.linkTwoVertices( 'B', 'F' );
   theGraph.linkTwoVertices( 'F', 'H' );
   theGraph.linkTwoVertices( 'D', 'G' );
   theGraph.linkTwoVertices( 'G', 'I' );

  # Do a depth first search on theGraph starting from 'A'
   searcher = DepthFirstSearcher( TEST_GRAPH_SIZE )
   print( "\n\n   Performing DFS traversal on graph beginning at vertex 'A': " )
   searcher.dfs( theGraph, 'A' )
   print( "                 Expecting: A B F H C D G I E" )
   print( "   Output list of vertices: " )
   for i in range( TEST_GRAPH_SIZE ):
      print( searcher.output[i], end=" " )
   print()

#      System.out.println( "\n\n   Starting over again, same graph, from 'G'... " );
#      theGraph = new Graph( TEST_GRAPH_SIZE );

#     // Create links between the Vertexs.
#      theGraph.linkTwoVertexs( 'A', 'B' );
#      theGraph.linkTwoVertexs( 'A', 'C' );
#      theGraph.linkTwoVertexs( 'A', 'D' );
#      theGraph.linkTwoVertexs( 'A', 'E' );
#      theGraph.linkTwoVertexs( 'B', 'F' );
#      theGraph.linkTwoVertexs( 'F', 'H' );
#      theGraph.linkTwoVertexs( 'D', 'G' );
#      theGraph.linkTwoVertexs( 'G', 'I' );
#      index = 0;
#      System.out.println( "\n\n   Performing DFS traversal on graph beginning at vertex 'G': " );
#      dfs( theGraph, 'G' );
#      System.out.println( "                 Expecting: G D A B F H C E I" );
#      System.out.print( "   Output list of vertices: " );
#      for( int i = 0; i < TEST_GRAPH_SIZE; i++ ) {
#        System.out.print( output[i] + " " );
#      }
#      System.out.println( );

main()
