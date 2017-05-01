import pydot
import pprint
pp = pprint.PrettyPrinter(indent=4)
graph_directed = pydot.graph_from_dot_file('test1.gv')

for dot in graph_directed:
    for node in dot.get_nodes():
        print node.get_name()
    for edge in dot.get_edges():
        print edge.get_label()