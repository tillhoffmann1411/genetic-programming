import pygraphviz as pgv

def plot_tree(nodes, edges, labels, name: str = "tree"):
  g = pgv.AGraph()
  g.add_nodes_from(nodes)
  g.add_edges_from(edges)
  g.layout(prog="dot")

  for i in nodes:
      n = g.get_node(i)
      n.attr["label"] = labels[i]

  name = name + '.png'
  g.draw('images/' + name)


def write_file(tree):
  f = open("gen_code.py", "a")
  f.write("# GP generated code\n" + str(tree) + "\n")
