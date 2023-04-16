/**
 *  File Name  :  DepthFirstSearcher.java
 *  Purpose    :  Provide a class for a depth first search of a graph
 *  Author     :  B.J. Johnson
 *  Date       :  26-Mar-2003
 *  Description:  This class performs a recursive depth-first search on a
 *    graph that is constructed with a user-entered number of nodes.  The
 *    graph is expected to be of the associated "graph" class.
 *
 *    Operation is recursive; at each level, all the Vertexs in the graph are
 *    checked for connectivity with the current Vertex.  The first Vertex that
 *    is connected is used as the root of the next recursion.  Vertexs are
 *    implemented as an adjacency matrix, in a pretty standard method.
 *    There is a boolean array to keep track of which Vertexs have been visited.
 *    A number of methods for performing the operation are also available.
 *    All of these items are part of the Graph.java class which is associated.
 *    This class actually creates and connects the graph to be searched.  It
 *    performs all the initializations, then does the search and lists the
 *    Vertexs as they become the root at each level of the recursion.  It's
 *    pretty basic, but it shows the idea.
 *
 */

public class DepthFirstSearcher   {

   private static final boolean DEBUG_ON = false;
   private static final int TEST_GRAPH_SIZE = 9;
   private static char [] output = new char[TEST_GRAPH_SIZE];
   private static int index = 0;

  // Do a depth first search on theGraph from a specified Vertex.  The Vertex that
  //  is passed as an argument is used as the root in the recursive search.
   public static void dfs( Graph theGraph, char currentVertex ) {
     // Mark the current Vertex ("me") as visited and print its name
      theGraph.markVisited( currentVertex );
      System.out.println( "  ** Visited " + currentVertex + " **" );
      output[index++] = currentVertex;

     // Try all the Vertexs in the graph in the following way:
     //  if there is a Vertex connected to me, if that Vertex hasn't been visited
     //  already, then mark it visited and do a [recursive] depth first search
     //  on the sub-graph with that Vertex as the root
      for( char nextVertex = 'A'; nextVertex <= ('A' + TEST_GRAPH_SIZE - 1); nextVertex++ ) {
         if( DEBUG_ON ) System.out.print( "  Checking " + nextVertex + " >> " );

         if( theGraph.areTwoVertexsConnected( currentVertex, nextVertex ) ) {

            if( DEBUG_ON ) System.out.println( "  Vertexs " + currentVertex + " and " + nextVertex + " ARE connected." );

            if( !theGraph.wasVisited( nextVertex ) ) {

               if( DEBUG_ON ) System.out.println( "Searching with " + nextVertex + " as root of tree." );

               dfs( theGraph, nextVertex );   // <-- HERE'S THE RECURSION!!

            } else {

               if( DEBUG_ON ) System.out.println( "    But Vertex " + nextVertex + " was already visited." );

            }
         } else {

            if( DEBUG_ON ) System.out.println( "  Vertexs " + currentVertex + " and " + nextVertex + " are NOT connected." );

         }
      }
   }

  /**
   *  MAIN
   *   The main method declares a graph of 9 Vertexs, initializes them and their
   *   connections, then performs a DFS on the graph just listing out the Vertexs
   *   as they are visited.  It also shows the checks
   */
   public static void main( String [] args )
   {
     // Create a new graph wih 8 Vertexs, which will be named 'A' through 'I'
      Graph theGraph = new Graph( TEST_GRAPH_SIZE );

     // Create links between the Vertexs.
      theGraph.linkTwoVertexs( 'A', 'B' );
      theGraph.linkTwoVertexs( 'A', 'C' );
      theGraph.linkTwoVertexs( 'A', 'D' );
      theGraph.linkTwoVertexs( 'A', 'E' );
      theGraph.linkTwoVertexs( 'B', 'F' );
      theGraph.linkTwoVertexs( 'F', 'H' );
      theGraph.linkTwoVertexs( 'D', 'G' );
      theGraph.linkTwoVertexs( 'G', 'I' );

     // Do a depth first search on theGraph starting from 'E'
      System.out.println( "\n\n   Performing DFS traversal on graph beginning at vertex 'A': " );
      dfs( theGraph, 'A' );
      System.out.println( "                 Expecting: A B F H C D G I E" );
      System.out.print( "   Output list of vertices: " );
      for( int i = 0; i < TEST_GRAPH_SIZE; i++ ) {
        System.out.print( output[i] + " " );
      }
      System.out.println( );

      System.out.println( "\n\n   Starting over again, same graph, from 'G'... " );
      theGraph = new Graph( TEST_GRAPH_SIZE );

     // Create links between the Vertexs.
      theGraph.linkTwoVertexs( 'A', 'B' );
      theGraph.linkTwoVertexs( 'A', 'C' );
      theGraph.linkTwoVertexs( 'A', 'D' );
      theGraph.linkTwoVertexs( 'A', 'E' );
      theGraph.linkTwoVertexs( 'B', 'F' );
      theGraph.linkTwoVertexs( 'F', 'H' );
      theGraph.linkTwoVertexs( 'D', 'G' );
      theGraph.linkTwoVertexs( 'G', 'I' );
      index = 0;
      System.out.println( "\n\n   Performing DFS traversal on graph beginning at vertex 'G': " );
      dfs( theGraph, 'G' );
      System.out.println( "                 Expecting: G D A B F H C E I" );
      System.out.print( "   Output list of vertices: " );
      for( int i = 0; i < TEST_GRAPH_SIZE; i++ ) {
        System.out.print( output[i] + " " );
      }
      System.out.println( );

   }
}
