import networkx as nx
class graph:
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        '''a method that performs a breadth first traversal and pathfinding on graph G'''
        if len(self.graph.nodes) == 0: 
            return None  # return an None if the graph is empty 

        if start not in self.graph.nodes:  
            raise ValueError("invalid node")  # return None if start node isn't in the graph 

        ''' * If there's no end node input, return a list of nodes with the order of BFS traversal '''
        if end is None:
            path = list(nx.bfs_tree(self.graph, start).nodes) # turns the undirected self.graph into a directed graph where parent nodes can be specifeid
            return path

        if end in self.graph.nodes:  
            if nx.has_path(self.graph, start, end): # looking for path between start and end nodes in the self.graph
                ''' * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path '''
                path = nx.shortest_path(self.graph, source=start, target=end)
                return path
            else:
                ''' * If there is an end node input and a path does not exist, return None '''
                return None

        else:
            return None  # return None if end node not in graph
"""
in the if nx.has_path() loop, if the graph is unconnected, BFS would start at the start node, 
but because there's no path to the end node, the code would just return None

this handles the edge case of: running bfs traversal on an unconnected graph
"""
