from graph import Graph
from util import Queue

def earliest_ancestor(ancestors, starting_node):
	graph = Graph()

	added = []

	for pair in ancestors:
		for item in pair:
			if item not in added:
				graph.add_vertex(item)
				added.append(item)

	for i in ancestors:
		graph.add_edge(i[1], i[0])

	for edge in graph.vertices:
		print(19, graph.vertices)
		pass

	revisited = graph.bft(starting_node)
	last = revisited[-1]
	if last == starting_node:
		return -1
	else:
		print(23, last)
		return last


# ---------------------------------

	# for i in ancestors:
	# 	parent = i[0]
	# 	child = i[1]
	# 	if parent in graph.vertices and child not in graph.vertices:
	# 		graph.add_vertex(child)
	# 	elif child in graph.vertices and parent not in graph.vertices:
	# 		graph.add_vertex(parent)
	# 	elif parent in graph.vertices and child in graph.vertices:
	# 		pass
	# 	else:
	# 		graph.add_vertex(parent)
	# 		graph.add_vertex(child)


	# for pair in ancestors:
	# 	parent = pair[0]
	# 	child = pair[1]

	# 	graph.add_vertex(parent)
	# 	graph.add_vertex(child)

	# 	graph.add_edge(child, parent)

	# qq = Queue()
	# qq.enqueue([starting_node])

	# longest_path = 1
	# earliest_ancestor = -1

	# while qq.size() > 0:
	# 	path = qq.dequeue()
	# 	current_node = path[-1]

	# 	if len(path) >= longest_path and current_node < earliest_ancestor or len(path) > longest_path: 

	# 		longest_path = len(path)
	# 		earliest_ancestor = current_node

	# 	neighbors = graph.vertices[current_node]
		
	# 	for ancestor in neighbors:
	# 		path_copy = list(path)
	# 		path_copy.append(ancestor)
	# 		qq.enqueue(path_copy)

	# print(62, path, earliest_ancestor)
	# return earliest_ancestor