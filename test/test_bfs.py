# write tests for bfs
import pytest
from search.graph import graph

def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    g = graph("data/tiny_network.adjlist")

    # choosing start node
    start_node = "Luke Gilbert" # first name in the file 

    # ran bfs on Luke Gilbert and got this (no end node):
    expected = ['Luke Gilbert', '33483487', '31806696', '31626775', '31540829', 'Martin Kampmann', 'Neil Risch', 'Nevan Krogan', '32790644', '29700475', '34272374', '32353859', '30944313', 'Steven Altschuler', 'Lani Wu', 'Michael Keiser', 'Atul Butte', 'Marina Sirota', 'Hani Goodarzi', '32036252', '32042149', '30727954', '33232663', '33765435', '33242416', '31395880', '31486345', 'Michael McManus', 'Charles Chiu', '32025019']

    # catching bfs results
    traversal = g.bfs(start=start_node) 

    # bfs on Luke Gilbert should result in expected
    assert traversal == expected, f"got {traversal} instead of {expected}"



def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """
    g = graph('data/citation_network.adjlist')
    
    # ran on 34413319 from (34413319;Nadav Ahituv) and got 31308376 as the last node in the list
    start_node = '34413319'
    end_node = '31308376'

    fast_traversal = g.bfs(start=start_node, end=end_node)
    
    short_path = ['34413319', 'Nadav Ahituv', '31784727', 'Ryan Hernandez', '32353859', 'Atul Butte', '33990806', 'Rima Arnaout', '31308376']

    assert fast_traversal == short_path, f"got {fast_traversal} instead of {short_path}"

    # node 34916529 and node 34858697 aren't connected, so running bfs should result in None
    assert g.bfs(start = "34916529", end = "34858697") == None, f"path found between {start_node} and {end_node} -- shouldn't be any"

    # including a test case that fails and raises an exception 
    with pytest.raises(ValueError, match="invalid node"):
        g.bfs(start="According to all known laws of aviation, there is no way that a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyways. Because bees don't care what humans think is impossible.")