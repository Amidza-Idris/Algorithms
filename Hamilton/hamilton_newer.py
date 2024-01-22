# Basic explanation of Hamilton path and cycle:
"""
Hamilton path - use each node at most once. (You can use the same edge multiple times, this applies to the cycle)
Hamilton cycle - make a full circle to the beggining node AND use each node at most once.
"""
# Usual approach to the problem would be to generate all possible paths and check if any of them satisfy given conditions,
# however that is stupid, I can do it better.


# Perform backtracking to check for paths. This is the backbone of the entire code. It is very hard to explain in a comment
# but here is a basic rundown:
"""
there are 4 variables: 
--- GRAPH (your dict graph), 
--- PATH (initialized in function is_cycle and  is_path [0, -1, -1...]), 
--- POS which is the sequential position of the path to take (the code trials and errors it's way to the correct path and in the 
is_hamilton function if it took the wrong path it will return to the previous node to see if it has other connections to 
it, if not it will go even more back... you get the point) and finally 
--- START which represents the starting node (the first key in your graph dict is initialized as start at the beggining)
"""
def is_hamilton(graph, path, pos, start):
    if pos == len(graph):        # If all vertices are visited, a path exists
        return True

    for v in graph[path[pos - 1]]:
        if v not in path:
            path[pos] = v        # Add the current node to the path
            if is_hamilton(graph, path, pos + 1, start):   # Recursively check the next node in the path
                return True
            path[pos] = -1       # Backtrack by removing the current node from the path
    return False                 # If no node leads to a solution, return False


# Function to check if hamilton cycle exists
def is_hamilton_cycle(graph):
    for start in graph:
        path = [-1] * len(graph)   # Initialize an array to store the paths, all starting paths are -1 for the first node
        path[0] = start            # Set the initial node for the hamilton path

        # Use the backtracking function to check for Hamilton path
        if is_hamilton(graph, path, 1, start) and path[len(graph) - 1] in graph[start]: # ↓
            # Check if the last node in the path has a connection to the first node, indicating a hamilton cycle
            return True
    return False   # No cycle?, False
# I could optimize the code by NOT REPEATING THE SAME PROCESS TWICE IF IT DOES NOT FIND A CYCLE, but it's late
# I need to sleep. I will do this some other time.


# Function to check if hamilton path exists, same as for the cycle pretty much with one less condition
def is_hamilton_path(graph):
    for start in graph:
        path = [-1] * len(graph)
        path[0] = start

        if is_hamilton(graph, path, 1, start):
            return True
    return False


# Function that initiates the check
def check_all(graph):
    if graph == {}:     # graph empty, no check for you
        print("Invalid graph")
        return
    if is_hamilton_cycle(graph):
        print("Graph has a hamilton cycle")
        print("Graph has a hamilton path")
        return      # if there is a circle then there is a path and we can skip the path check.
    else:
        print("Graph does not have a hamilton cycle")

    if is_hamilton_path(graph):
        print("Graph has a hamilton path")
    else:
        print("Graph does not have a hamilton path")

# Example usage:
# NOTES: There was a bug where if you didnt put dict's keys in indexing order (0, 1, 2, 3) the code wouldn't work.
# I have fixed it now, I think :)
# ALSO, i used the same graphs from euler to test hamilton, so if you want a visual representation you can go to Euler/Euler paths.png

graph_dict = {
    0: [1, 4], 
    1: [0, 2], 
    2: [1, 3, 5], 
    3: [2, 4, 6], 
    4: [3, 0],
    5: [2, 6],
    6: [5, 3]
}
check_all(graph_dict)

g1 = {
    0: [1, 2, 3], 
    1: [0, 2], 
    2: [0, 1], 
    3: [0, 4], 
    4: [3]
}
check_all(g1)

g2 = {
    1: [0, 2], 
    0: [1, 2, 3, 4], 
    2: [0, 1], 
    3: [0, 4], 
    4: [3, 0]
}
check_all(g2)

g3 = {
    1: [0, 2, 3], 
    0: [1, 2, 3], 
    2: [0, 1], 
    3: [0, 4, 1], 
    4: [3]
}
check_all(g3)

g5 = {}
check_all(g5)

g6 = {
    0: [1],
    1: [0],
    2: []
}
check_all(g6)
