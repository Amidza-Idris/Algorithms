def dijkstra(graph, start, end):
    # Dictionary where each node in the graph is a key, and the corresponding value is set to positive infinity
    # float('infinity') -- this is possible in python, since the interpreter doesnt actually assisgn a string value to a float, 
    #but rather a very high number.

    distances = {node: float('infinity') for node in graph} 
    print(distances)
    # print(float('infinity'))    # we can see the float('infinity') in action, it has value inf
    distances[start] = 0
    print(distances)
    visited = set()     # Initializes an empty set (has it's own functions), and it can accept a dict to display it as a set. the elements 
                        # are at random postions

    while visited != set(graph):
        current_node = min((node for node in graph if node not in visited), key=lambda x: distances[x])
        print(current_node)
        print(graph[current_node])

        for neighbor, weight in graph[current_node].items():
            if distances[current_node] + weight < distances[neighbor]:
                distances[neighbor] = distances[current_node] + weight

        visited.add(current_node)

    return distances[end]

# Example usage:
graph = {
    'A': {'B': 1, 'C': 4, 'E':1},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1, 'D': 1},
    'E': {'D': 1, 'A': 1}
}

# Loading data from txt

shortest_path_distance = dijkstra(graph, 'A', 'D')
print("Shortest Path Distance:", shortest_path_distance)




"""
# Dijkstra's Algorithm old version


import sys

# Providing the graph
vertices = [[0, 0, 1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 1, 0],
            [1, 1, 0, 1, 1, 0, 0],
            [1, 0, 1, 0, 0, 0, 1],
            [0, 0, 1, 0, 0, 1, 0],
            [0, 1, 0, 0, 1, 0, 1],
            [0, 0, 0, 1, 0, 1, 0]]

edges = [[0, 0, 1, 2, 0, 0, 0],
         [0, 0, 2, 0, 0, 3, 0],
         [1, 2, 0, 1, 3, 0, 0],
         [2, 0, 1, 0, 0, 0, 1],
         [0, 0, 3, 0, 0, 2, 0],
         [0, 3, 0, 0, 2, 0, 1],
         [0, 0, 0, 1, 0, 1, 0]]

# Find which vertex is to be visited next
def to_be_visited():
    global visited_and_distance
    v = -10
    for index in range(num_of_vertices):
        if visited_and_distance[index][0] == 0 \
            and (v < 0 or visited_and_distance[index][1] <=
                 visited_and_distance[v][1]):
            v = index
    return v


num_of_vertices = len(vertices[0])

visited_and_distance = [[0, 0]]
for i in range(num_of_vertices-1):
    visited_and_distance.append([0, sys.maxsize])

for vertex in range(num_of_vertices):

    # Find next vertex to be visited
    to_visit = to_be_visited()
    for neighbor_index in range(num_of_vertices):

        # Updating new distances
        if vertices[to_visit][neighbor_index] == 1 and \
                visited_and_distance[neighbor_index][0] == 0:
            new_distance = visited_and_distance[to_visit][1] \
                + edges[to_visit][neighbor_index]
            if visited_and_distance[neighbor_index][1] > new_distance:
                visited_and_distance[neighbor_index][1] = new_distance
        
        visited_and_distance[to_visit][0] = 1

i = 0

# Printing the distance
for distance in visited_and_distance:
    print("Distance of ", chr(ord('a') + i),
          " from source vertex: ", distance[1])
    i = i + 1
"""