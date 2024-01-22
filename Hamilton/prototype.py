def is_hamilton(graph, path, pos, start, check_cycle=True):
    if pos == len(graph):
        if check_cycle and path[len(graph) - 1] not in graph[start]:
            return False   # If checking for a cycle and the last node is not connected to the first, return False
        return True

    for v in graph[path[pos - 1]]:
        if v not in path:
            path[pos] = v
            if is_hamilton(graph, path, pos + 1, start, check_cycle):
                return True
            path[pos] = -1

    return False


def is_hamilton_cycle(graph):
    for start in graph:
        path = [-1] * len(graph)
        path[0] = start

        if is_hamilton(graph, path, 1, start):
            return True
    return False


def is_hamilton_path(graph):
    for start in graph:
        path = [-1] * len(graph)
        path[0] = start

        if is_hamilton(graph, path, 1, start, check_cycle=False):   # Don't check for a cycle in the path function
            return True
    return False
