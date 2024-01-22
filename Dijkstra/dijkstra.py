def dijkstra(graph, start, end):
    # Dictionary where each node in the graph is a key, and the corresponding value is set to positive infinity
    # float('infinity') -- this is possible in python, since the interpreter doesnt actually assisgn a string value to a float, 
    #but rather a very high number.

    distances = {node: float('infinity') for node in graph} 
    # print(float('infinity'))    # we can see the float('infinity') in action, it has value inf
    distances[start] = 0
    visited = set()     # Initializes an empty set (has it's own functions), and it can accept a dict to display it as a set. the elements 
                        # are at random postions

    while visited != set(graph):
        current_node = min((node for node in graph if node not in visited), key=lambda x: distances[x]) # Basically, takes a point and then
        # looks at its connections. it updates the distances for each point trough a lambda function. This can be written in the following way
        # to make it more understandable:
        """
        def get_distance_for_node(node):
            return distances[node]

        def find_next_node(graph, visited, distances):
            # This creates a list of unvisited nodes.
            unvisited_nodes = [node for node in graph if node not in visited]

#___________Equivelent to following code_____⇑___________________________________________________________________________
            def find_unvisited_nodes(graph, visited):
                unvisited_nodes = []

                # Iterate through all nodes in the graph and check if they are not in the visited set.
                for node in graph:
                    if node not in visited:
                        unvisited_nodes.append(node)

                return unvisited_nodes
            

            # Now you can use this function to get the list of unvisited nodes
            unvisited_nodes = find_unvisited_nodes(graph, visited)
#___________________________________________________________________________________________________________________________
         # Find the node with the minimum distance using the built-in min function and our named function.
            next_node = min(unvisited_nodes, key=get_distance_for_node)
            return next_node

        current_node = find_next_node(graph, visited, distances)
        """
        #print(current_node)              # current node (point we are looking at)
        #print(graph[current_node])       # Nodes conections to other nodes
        #print(distances)                 # Currently know lowest distances
        #print(distances[current_node])   # Distance to current node

        for neighbor, weight in graph[current_node].items():    # .items() basically iterates over the dictionary assigning both the key and value to the correct variables. If you don't put 2 variables it will put them in a list.
            #print(weight, neighbor, distances[neighbor])
            if distances[current_node] + weight < distances[neighbor]:  # if the travel cost from current node to next one is less then 
                distances[neighbor] = distances[current_node] + weight  # currently known dsitance, update that distance.

        visited.add(current_node)   # Since we are using while loop, we must update the visited, otherwise... infinity.

    return distances[end]   # after while loop is finished all known distances are updated and we can see shortest distance to each path
                            # but we only want to see the disteance to one specific point.

# Example graph:
graph = {
    'A': {'B': 1, 'C': 4, 'E':1},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1, 'D': 1},
    'E': {'D': 1, 'A': 1}
}

# Loading data from txt (To be implemented - gen_graph.py)

shortest_path_distance = dijkstra(graph, 'A', 'D')
print("Shortest Path Distance:", shortest_path_distance)
