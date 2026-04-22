import math


def dijkstra_tsp( graph, start = 0 ):
   num_vertices = len( graph )
   visited = [False] * num_vertices
   path = [start]
   total_cost = 0

   current = start
   visited[current] = True

   for _ in range( num_vertices - 1 ):
      nearest = None
      min_dist = math.inf

      for next_vertex in range( num_vertices ):
         if not visited[next_vertex] and graph[current][next_vertex] != 0:
            if graph[current][next_vertex] < min_dist:
               min_dist = graph[current][next_vertex]
               nearest = next_vertex

      visited[nearest] = True
      path.append( nearest )
      total_cost += min_dist
      current = nearest

   # Return to start
   total_cost += graph[current][start]
   path.append( start )

   return path, total_cost


def main():
   # Weighted graph as adjacency matrix
   # 0 means no self-loop, a vertex is not adjacent to itself
   graph = [
      [ 0, 10, 15, 20],
      [10,  0, 35, 25],
      [15, 35,  0, 30],
      [20, 25, 30,  0]
   ]

   print( "\n   The weighted graph is: \n", graph )

   path, cost = dijkstra_tsp(graph, start=0)

   print( "\n   Dijkstra TSP Path: ", end="" )
   print( " -> ".join( str( v ) for v in path ) )
   print( "   Total Cost:", cost )


if __name__ == "__main__":
   main()
