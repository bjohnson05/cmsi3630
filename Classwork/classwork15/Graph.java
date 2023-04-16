/**
 *  File Name  :  Graph.java
 *  Purpose    :  Provide a Graph class for the depth first search demo
 *  Author     :  Dr. Johnson
 *  Date       :  26-Mar-2003
 *  Description:  This class is the graph class which is the companion
 *                   to the DepthFirstSearcher class.
 *
 *  This graph is represented simply as an adjacency matrix array.  The
 *    array is dimensioned as "n-by-n" where "n" is the number of vertexs
 *    in the graph.  The graph is initialized by marking two vertexs as
 *    connected in the adjacency matrix.
 *
 */

public class Graph   {
   private int   [][] adjaMatrix; // The adjacency matrix represents the graph
   private boolean [] visited;    // Element is true if vertex is visited

  // Constructor for the graph; this just declares the arrays, then
  //  simply initializes the adjacency matrix to all zeroes
   public Graph( int numVertexs )   {
      adjaMatrix = new int[numVertexs][numVertexs];
      visited    = new boolean[numVertexs];

     // Initialize all adjacency elements to zero (just insurance since ints
     //  are automatically initialized to zero), and initialize the visited
     //  array to all false
      for( int i = 0; i < adjaMatrix.length; i ++ )   {
         visited[i] = false;
         for( int j = 0; j < adjaMatrix[i].length; j ++ )   {
            adjaMatrix[i][j] = 0;
         }
      }
   }

  // Mark two vertexs as connected.  This is done by putting a "1" in
  //  each of the cells in the adjacency matrix for the two connected vertexs
   public void link( int vertexName1, int vertexName2 )   {
      adjaMatrix[vertexName1][vertexName2] = 1;
      adjaMatrix[vertexName2][vertexName1] = 1;
   }

  // Make a link between two vertexs by calling the "link()" method with
  //  their converted indices; note that we have to FIND each vertex's index
   public void linkTwoVertexs( char vertexOne, char vertexTwo )   {
      link( convertToIndex(vertexOne), convertToIndex(vertexTwo) );
   }

  // Check if this vertex has been visited already
   public boolean wasVisited( char vertex )   {
      int index = convertToIndex( vertex );   // Calculate the vertex index
      return( visited[index] );             // Return the array value
   }

  // Mark a vertex as having been visited
   public void markVisited( char vertex )   {
      visited[convertToIndex( vertex )] = true;
   }

  // Calculate a vertex's index based on its letter name (ASCII)
   public int convertToIndex( char vertexName ) {
      return( vertexName - 'A' );
   }

  // Check if two vertexs are connected
   public boolean areTwoVertexsConnected( char vertexOne, char vertexTwo )   {
      return( adjaMatrix[convertToIndex(vertexOne)]
                        [convertToIndex(vertexTwo)] == 1 );
   }
}
