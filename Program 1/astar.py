def AStart(startnode, stopnode):
    openlist = set(startnode)
    closelist = set()
    g = {}  # Stores the heurisitc values
    g[startnode] = 0
    parents = {}
    parents[startnode] = startnode

    while len(openlist) > 0:
        node = None
        for vertex in openlist:
            if node == None or g[vertex] + heuristic(vertex) < g[node] < heuristic(node):
                node = vertex

        if node == stopnode or Graph_nodes[node] == None:
            pass

        else:
            for (neighbor, weight) in get_neighbors(node):
                if neighbor not in openlist and neighbor not in closelist:
                    openlist.add(neighbor)
                    parents[neighbor] = node
                    g[neighbor] = g[node] + weight
                else:
                    if g[neighbor] > g[node] + weight:
                        g[neighbor] = g[node] + weight
                        parents[neighbor] = node
                        if neighbor in closelist:
                            closelist.remove(neighbor)
                            openlist.add(neighbor)

        if node == None:
            print('Path not found')
            return None

        if node == stopnode:
            path = []
            while parents[node] != node:
                path.append(node)
                node = parents[node]
            path.append(startnode)
            path.reverse()
            print('Path found: {}'.format(path))
            return path

        openlist.remove(node)
        closelist.add(node)
    print('Path doesn\'t exist')
    return None


def get_neighbors(vertex):
    if vertex in Graph_nodes:
        return Graph_nodes[vertex]
    else:
        return None


def heuristic(node):
    H_dist = {
        'A': 10,
        'B': 8,
        'C': 5,
        'D': 7,
        'E': 3,
        'F': 6,
        'G': 5,
        'H': 3,
        'I': 1,
        'J': 0
    }
    return H_dist[node]


Graph_nodes = {
    'A': [('B', 6), ('F', 3)],
    'B': [('C', 3), ('D', 2)],
    'C': [('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 8)],
    'E': [('I', 5), ('J', 5)],
    'F': [('G', 1), ('H', 7)],
    'G': [('I', 3)],
    'H': [('I', 2)],
    'I': [('E', 5), ('J', 3)],
}

AStart('A', 'J')