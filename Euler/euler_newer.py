# Basic explanation of Euler path and cycle:
"""
Euler path - use each edge (connection) at most once. (You can land in the same node multiple times, this applies to the cycle)
Euler cycle - make a full circle to the beggining node AND use each edge (connection) at most once.
"""

# Depth-first search function to navigate the graph and mark visited nodes.
def dfs_util(graph, v, visited):
    visited[v] = True       # Mark the current node as visited
    for i in graph[v]:      # Look at the neighbors of the current node
        if not visited[i]:  # If the neighbor is not visited, go ahead and visit it with recursion call dfs_util
            dfs_util(graph, i, visited)


# Check connection between nodes
def is_connected(graph, vertices):
    visited = [False] * vertices  # List of visited nodes

    for i in range(vertices):
        if len(graph.get(i, [])) != 0:  # Find first node with non-zero degree (this means that the node has at least one edge - connection to a different node)
            break
    if i == vertices - 1:  # If all nodes have zero degree (i know confusing, basically if all nodes have some connection, oposite of non-zero degree), the graph is connected
        return True

    dfs_util(graph, i, visited)  # Navigate from the first non-zero degree node (few things to note, the "i" should always be 0 and the "visited" list should be filled with False before alling DFS)
    for i in range(vertices):
        if not visited[i] and len(graph.get(i, [])) > 0:  # Check if all non-zero degree nodes have been visited
            return False
    return True


# Checking if the graph is anything important lol
def is_eulerian(graph, vertices):
    if not is_connected(graph, vertices):  # If the graph is not connected, it can't be Eulerian
        return 0
    else:
        # Count the number of nodes with an odd degree. This is actually the main part. You could theoretically determine the graphs property with only this code.
        odd = 0
        for i in range(vertices):
            if len(graph.get(i, [])) % 2 != 0:  # len(graph.get(i, [])) is very interesting. i is the 'key' for the dictionary value and .get sortof appends the key's value into the empty list next to i. then it gets length and yea
                odd += 1

        # Euler common theory
        if odd == 0:  # If there are no nodes with an odd degree, the graph has an Euler cycle
            return 2
        elif odd == 2:  # If there are exactly two nodes with an odd degree, the graph has an Euler path
            return 1
        elif odd > 2:  # If there are more than two nodes with an odd degree, the graph is not Eulerian
            return 0


# This just prints the result and does checks and setups.
def test_graph(graph):
    if graph == {}:  # Check if the graph is empty, no point to processing
        print("Invalid graph.")
        return
    res = is_eulerian(graph, len(graph))  # Initiate processing :)
    if res == 0:
        print("graph is not Eulerian")
    elif res == 1:
        print("graph has an Euler path")
    else:
        print("graph has an Euler cycle")


# TESTING:
# NOTES: There is a small glitch where you can add the 2 completly same edges and the code will treat them as if they were two completly 
# diffrent edges. I will probably fix this later (with gen_graph GUI), but for now it doesn't seem to cause any issues, other then longer processing time

g1 = {
    0: [1, 2, 3], 
    1: [0, 2], 
    2: [0, 1], 
    3: [0, 4], 
    4: [3]
}
test_graph(g1)

g2 = {
    1: [0, 2], 
    0: [1, 2, 3, 4], 
    2: [0, 1], 
    3: [0, 4], 
    4: [3, 0]
}
test_graph(g2)

g3 = {
    1: [0, 2, 3], 
    0: [1, 2, 3], 
    2: [0, 1], 
    3: [0, 4, 1], 
    4: [3]
}
test_graph(g3)

g4 = {
    0: [1, 2], 
    1: [0, 2], 
    2: [1, 0]
}
test_graph(g4)

g5 = {}
test_graph(g5)

g6 = {
    0: [1],
    1: [0],
    2: []
}
test_graph(g6)