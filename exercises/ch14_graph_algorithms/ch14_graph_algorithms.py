"""
chapter 14: graph algorithms 
"""
from Partition import Partition

import sys, os
sys.path.append(os.path.abspath("D:\Projects\data_structures_and_algorithms_in_python\exercises\ch09_priority_queues"))

from AdaptableHeapPriorityQueue import AdaptableHeapPriorityQueue
from HeapPriorityQueue import HeapPriorityQueue


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

# edge = [('u','v','e'), ('u','w','g'), ('v','w','f'), ('w','z','h')]
# for u,v,x in edge:
    # u_obj = vertex_obj[u]
    # v_obj = vertex_obj[v]
    # g.insert_edge(u_obj, v_obj, x)

# weighted graph     
edge = [('u','v','e'), ('u','w','g'), ('v','w','f'), ('w','z','h')]
for u,v,x in edge:
    u_obj = vertex_obj[u]
    v_obj = vertex_obj[v]
    g.insert_edge(u_obj, v_obj, ord(x))    
    
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
    
    
# P 676 
# transitive closure 
# transitive closure of a directed graph G is itself a directed graph G'
# such that the vertices of G are the same as the vertices of G'
# G' has an edge (u,v), whenever G has a directed path from u to v (including the case where (u,v) is an edge of the original G  

# Transitive closure of a graph. Given a directed graph, find out if a vertex j is reachable from another vertex i for all vertex pairs (i, j) in the given graph. Here reachable mean that there is a path from vertex i to j. The reach-ability matrix is called transitive closure of a graph.
from copy import deepcopy

def floyd_warshall(g):
    """
    return a new graph that is the transitive closure of g 
    """
    closure = deepcopy(g)  # import from copy module 
    verts = list(closure.vertices())  # make indexable list 
    n = len(verts)
    for k in range(n):
        for i in range(n):
            # verify that edge (i, k) exists in the partial closure 
            if i != k and closure.get_edge(verts[i], verts[k]) is not None:
                for j in range(n):
                    # verify that edge (k,j) exists in the partial closure 
                    if i != j != k and closure.get_edge(verts[k], verts[j]) is not None:
                        # if (i,j) not yet included, add it the closure 
                        if closure.get_edge(verts[i], verts[j]) is None:
                            closure.insert_edge(verts[i], verts[j])
    return closure 

print('-' * 20)
c = floyd_warshall(g)
cv = c.vertices()
ce = c.edges()
print('transitive closure of g:')
print(f'vertices: {[v._element for v in cv]}')  
print(f'edges: {[e._element for e in ce]}')  


# P 677
# topological sorting algorithm 
def topological_sort(g):
    """
    return a list of verticies of directed acyclic graph g in topological order 
    
    if graph g has a cycle, the result will be incomplete 
    """
    topo = []  # a list of vertices placed in topological order 
    ready = []  # list of vertices that have no remaining constraints 
    incount = {}  # keep track of in-degree for each vertex 
    for u in g.vertices():
        incount[u] = g.degree(u, False)  # parameter requests incoming degree 
        if incount[u] == 0:
            ready.append(u)
    while len(ready) > 0:
        u = ready.pop()  # u is free of constraints  
        topo.append(u)  # add u to the topological order 
        for e in g.incident_edges(u):  # consider all outgoing neighbors of u 
            v = e.opposite(u)
            incount[v] -= 1  # v has one less constraint without u 
            if incount[v] == 0:
                ready.append(v)
    return topo 
    
print('-'*20)
print(topological_sort(g))  # g has cycle, return []
    
    
# P 683 
# Dijkstra's algorithm: greedy method  
"""
- single-source  
- define a label D[v] for each vertex v --> approximate the distance from s to v  
- the length of the best path from s to v so far  
- D[s]=0 and D[v]=∞ for each v!=s  
- relaxation: add a new vertex, update the label D[v] of each vertex v  
"""


# Python implementation of Dijkstra’s algorithm for computing the shortest-path distances from a single source. We assume that e.element() for edge e represents the weight of that edge

def shortes_path_lengths(g, src):
    """
    compute shortest path distances from src to reachable vertices of g 
    
    graph g can be undirected or directed, but must be weighted such that e.element() returns a numeric weight for each edge e 
    
    return dictionary mapping each reachable vertex to its distance from src 
    """
    d = {}  # d[v] is upper bound from s to v 
    cloud = {}  # map reachable v to its d[v] value 
    pq = AdaptableHeapPriorityQueue()  # vertex v will have key d[v]  
    pqlocator = {}  # map from vertex to its pq locator 
    
    # for each vertex v of the graph add an entry to the priority queue with the source having distance 0 and all others having infinite distance 
    for v in g.vertices():
        if v is src:
            d[v] = 0
        else:
            d[v] = float('inf')  # syntax for positive infinity 
        pqlocator[v] = pq.add(d[v], v)  # save locator for future updates 
    
    while not pq.is_empty():
        key, u = pq.remove_min()
        cloud[u] = key  # correct d[u] value 
        del pqlocator[u]  # u is no longer in pq  
        for e in g.incident_edges(u):
            v = e.opposite(u)
            if v not in cloud:
                # perform relaxation step on edge (u, v)
                wgt = e.element()
                if d[u] + wgt < d[v]:  # better path to v 
                    d[v] = d[u] + wgt  # update the distance 
                    pq.update(pqlocator[v], d[v], v)  # update the pq entry 
    return cloud  # only includes reachable vertices 
    
print('-'*20)  
src = vertex_obj['v']  # source node 
# shortest path for each node in the graph 
short = shortes_path_lengths(g, src)
print('shortest path for each node:')
for v in short: 
    print(f'{v._element}: {short[v]}')

    
    
# P 691  
# function that reconstructs the shortest paths based on knowledge of the single-source distances 
def shortest_path_tree(g, s, d):
    """
    reconstruct shortest-path tree rooted at vertex s, given distance map d 
    
    return tree as a map from each reachable vertex v (other than s) to the edge e=(u,v) that is used to each v from its parent u in the tree 
    """
    tree = {}
    for v in d:
        if v is not s:
            for e in g.incident_edges(v, False):  # consider incoming edges 
                u = e.opposite(v)
                wgt = e.element()
                if d[v] == d[u] + wgt:
                    tree[v] = e  # edge e is used to reach v 
    return tree 
    
print('-'*20)
print('shortest path tree: ')
tree = shortest_path_tree(g, src, short)
for v in tree:
    print(f'vertex: {v._element}, edge: {tree[v]._element}')
    
# P 694    
# Prim-Jarnik algorithm
# grow a minimum spanning tree from a single cluster starting from root vertex s
def MST_PrimJarnik(g):
    """
    compute a minimum spanning tree of weighted graph g 
    
    return a list of edges that comprise the MST in arbitrary order 
    """
    d = {}  # d[v] is bound on distance to tree 
    tree = []  # list of edges in spanning tree 
    pq = AdaptableHeapPriorityQueue()  # d[v] maps to value (v, e=(u,v))
    pqlocator = {}  # map from vertex to its pq locator 
    
    # for each vertex v of the graph add an entry to the priority queue with the source having distance 0 and all other s have infinite distance  
    for v in g.vertices():
        if len(d) == 0:  # this is the first node 
            d[v] = 0  # make it the root 
        else:
            d[v] = float('inf')  # positive infinity 
        pqlocator[v] = pq.add(d[v], (v, None))
        
    while not pq.is_empty():
        key, value = pq.remove_min()
        u, edge = value  # unpack tuple from pq 
        del pqlocator[u]  # u is no longer in pq 
        if edge is not None:
            tree.append(edge)  # add edge to tree 
        for link in g.incident_edges(u):
            v = link.opposite(u)
            if v in pqlocator:
                # see if edge (u,v) better connects v to the growing tree 
                wgt = link.element()
                if wgt < d[v]:  # better edge to v ?
                    d[v] = wgt  # update the distance 
                    pq.update(pqlocator[v], d[v], (v, link))  # update the pq entry 
    return tree 
    
print('-'*20)
t = MST_PrimJarnik(g)
print(f'MST_PrimJarnik: {[e._element for e in t]}')  


# P 698
# Kruskal's algorithm 
# growing a single tree until it spans the graph --> maintains a forest of clusters, repeatedly merging pairs of clusters until a single cluster spans the graph 
def MST_Kruskal(g):
    """
    compute a minimum spanning tree of a graph using Kruskal's algorithm 
    return a list of edges that comprise the MST 
    the elements of the graph's edges are assumed to be weights 
    """
    tree = []  # list of edges in spanning tree 
    pq = HeapPriorityQueue()  # entries are edges in G with weights as key 
    forest = Partition() # keeps track o forest clusters 
    position = {}  # map each node to its Partition entry 
    
    for v in g.vertices():
        position[v] = forest.make_group(v)
        
    for e in g.edges():
        pq.add(e.element(), e)  # edge's element is assumed to be its weight 
        
    size = g.vertex_count()
    while len(tree) != size - 1 and not pq.is_empty():
        # tree not spanning and unprocessed edges remain 
        weight, edge = pq.remove_min()
        u, v = edge.endpoints()
        a = forest.find(position[u])
        b = forest.find(position[v])
        if a != b:
            tree.append(edge)
            forest.union(a, b)
    return tree         
            
    
print('-'*20)
t = MST_Kruskal(g)
print(f'MST_Kruskal: {[e._element for e in t]}')
