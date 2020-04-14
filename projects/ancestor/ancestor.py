from graph import Graph

"""
 10
 /
1   2   4  11
 \ /   / \ /
  3   5   8
   \ / \   \
    6   7   9
"""


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()



	for i in ancestors:
		if i[0] in graph.vertices and i[1] not in graph.vertices:
			graph.add_vertex(i[1])
		elif i[1] in graph.vertices and i[0] not in graph.vertices:
			graph.add_vertex(i[0])
		elif i[0] in graph.vertices and i[1] in graph.vertices:
			pass:
		else:
			graph.add_vertex(i[0])
			graph.add_vertex(i[1])
		
	for i in ancestors:
		graph.add_edge(i[1], i[0])

	revisited = graph.bft(starting_node)
	last = revisited[-1]
	if last == starting_node:
		return -1
	else:
		return last