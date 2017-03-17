"""
chapter 14: graph algorithms 
"""

# P 659
# test Graph class 
from Graph import Graph

"""
*             0 1 2 3  
* (u) --> 0 |   e g  |  
* (v) --> 1 | e   f  |  
* (w) --> 2 | g f   h|  
* (z) --> 3 |     h  |  
"""
g = Graph(directed=False)
vertex = ['u', 'v', 'w', 'z']
vertex_obj = {}
for v in vertex:
    v_obj = g.insert_vertex(v)
    vertex_obj[v] = v_obj
'''
# vertex_obj
{'u': <Graph.Vertex object at 0x000001B15E3B9768>, 'v': <Graph.Vertex object at 0x000001B15E3B97F8>, 'w': <Graph.Vertex object at 0x000001B15E3B9858>, 'z': <Graph.Vertex object at 0x000001B15E3B9978>}
'''
    
# is directed or not    
print(f'directed? {g.is_directed()}')    
# number of vertices    
print(f'number of vertices: {g.vertex_count()}')    
# all vertices of the graph
print([v._element for v in g.vertices()])

edge = [('u','v','e'), ('u','w','g'), ('v','w','f'), ('w','z','h')]
for u,v,x in edge:
    u_obj = vertex_obj[u]
    v_obj = vertex_obj[v]
    g.insert_edge(u_obj, v_obj, x)
    
# number of edges 
print(f'number of edges: {g.edge_count()}')
# all edges of the graph 
print([(e._origin._element, e._destination._element, e._element) for e in g.edges()])

# degree
for v in vertex_obj:
    print(f'degree of {v}: {g.degree(vertex_obj[v])}')

# incident edges 
v = 'v'
v_obj = vertex_obj[v]
a = g.incident_edges(v_obj)  # get the adjacent edges of v 
print(f"incident edges of vertex {v}:", end=" ")
for e in a:
    print(e._element, end=" ")
print()


# P 666
# depth-first search 
# recursive implementation of depth-first search on a graph starting at a designated vertex u  
def DFS(g, u, discovered):
    """
    perform DFS of the undiscovered portion of Graph g starting at Vertex u
    
    discovered is a dictionary mapping each vertex to the edge that was used to
    discover it during the DFS. (u should be "discovered" prior to the call.)
    Newly discovered vertices will be added to the dictionary as a result.
    """
    for e in g.incident_edges(u):  # for every outgoing edge from u 
        v = e.opposite(u)
        if v not in discovered:  # v is an unvisited vertex 
            discovered[v] = e  # e is the tree edge that discovered v 
            DFS(g, v, discovered)  # recursively explore from v 


    
print('-'*20)
result = {v_obj: None}  # a new dictionary, with v trivially discovered 
DFS(g, v_obj, result)
print('depth-first search: ')
for v in result:
    n = v._element
    e = result[v]._element if result[v] is not None else None 
    print(f'vertex: {n} edges: {e}')
    
    
    
# P 667
# Function to reconstruct a directed path from u to v, given the trace of discovery from a DFS started at u. 
# The function returns an ordered list of vertices on the path
def construct_path(u, v, discovered):
    """
    - begin at the end of the path, examining the discovery dictionary to determine what edge was used to reach vertex v
    - traced the path all the way back to the starting vertex u
    - reverse the list so that it is properly oriented from u to v
    """
    path = []  # empty path by default 
    if v in discovered:
        # if v in discovered, build list from v to u and then reverse it at the end 
        path.append(v)
        walk = v
        while walk is not u:
            e = discovered[walk]  # find edge leading to walk
            parent = e.opposite(walk)
            path.append(parent)
            walk = parent
        path.reverse()  # reorient path from u to v 
    return path 

print('-'*20)    
a = 'v'
a_obj = vertex_obj[a]
b = 'z'
b_obj = vertex_obj[b]
p = construct_path(a_obj, b_obj, result)
print(f'path from {a} to {b}: {[ver._element for ver in p]}' )


# P 668
# Top-level function that returns a DFS forest for an entire graph
def DFS_complete(g):
    """
    perform DFS for entire graph and return forest as a dictionary 
    result maps each vertex v to the edge that was used to discover it. 
    (vertices that are roots of a DFS tree are mapped to None) 
    """
    forest = {}
    for u in g.vertices():
        if u not in forest:
            forest[u] = None  # u will be the root of the tree
            DFS(g, u, forest)
    return forest

print('-'*20)
f = DFS_complete(g)
print(f'forest: {[ver._element for ver in f]}')    
    
# P 670
# breadth-first search 
# implementation of breadth-first search on a graph, starting at a designated vertex s 
def BFS(g, s, discovered):
    """
    perform BFS of the undiscovered portion of Graph g starting at Vertex s 
    
    discovered is a dictionary mapping each vertex to the edge that was used to discover it during the BFS (s should be mapped None prior to the call)
    Newly discovered vertices will be added to the dictionary as a result 
    """
    level = [s]  # first level includes only s 
    while len(level) > 0:
        next_level = []  # prepare to gather newly found vertices 
        for u in level:
            for e in g.incident_edges(u):  # for every outgoing edge from u 
                v = e.opposite(u)
                if v not in discovered:  # v is an unvisited vertex 
                    discovered[v] = e  # e is the tree edge that discovered v 
                    next_level.append(v)  # v will be further considered in next pass 
        level = next_level  # relabel 'next' level to become current  
        
print('-'*20)        
result_bfs = {v_obj: None}  # a new dictionary, with v trivially discovered
BFS(g, v_obj, result_bfs)
print('breadth-first search: ')
for v in result_bfs:
    n = v._element
    e = result[v]._element if result[v] is not None else None 
    print(f'vertex: {n} edges: {e}')