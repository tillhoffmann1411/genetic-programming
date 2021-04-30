from deap.tools.support import Logbook
import matplotlib.pyplot as plt
import pygraphviz as pgv


def plot(log: Logbook):
  gen = log.select("gen")
  fit_mins = log.chapters["fitness"].select("min")
  size_avgs = log.chapters["size"].select("avg")

  fig, ax1 = plt.subplots()
  line1 = ax1.plot(gen, fit_mins, "b-", label="Minimum Fitness")
  ax1.set_xlabel("Generation")
  ax1.set_ylabel("Fitness", color="b")
  for tl in ax1.get_yticklabels():
      tl.set_color("b")

  ax2 = ax1.twinx()
  line2 = ax2.plot(gen, size_avgs, "r-", label="Average Size")
  ax2.set_ylabel("Size", color="r")
  for tl in ax2.get_yticklabels():
      tl.set_color("r")

  lns = line1 + line2
  labs = [l.get_label() for l in lns]
  ax1.legend(lns, labs, loc="center right")
  plt.show()

def plot_tree(nodes, edges, labels, name: str = "tree"):
  g = pgv.AGraph()
  g.add_nodes_from(nodes)
  g.add_edges_from(edges)
  g.layout(prog="dot")

  for i in nodes:
      n = g.get_node(i)
      n.attr["label"] = labels[i]

  name = name + '.png'
  g.draw(name)


def write_file(tree):
  f = open("gen_code.py", "a")
  f.write("# GP generated code\n" + str(tree) + "\n")


def is_prime(num: float):
  # define a flag variable
  flag = False

  # prime numbers are greater than 1
  if num > 1:
      # check for factors
      for i in range(2, num):
          if (num % i) == 0:
              # if factor is found, set flag to True
              flag = True
              # break out of loop
              break
  return flag


def if_then_else(input, output1, output2):
  return output1 if is_prime(input) else output2

def protectedDiv(left, right):
    try:
        return left / right
    except ZeroDivisionError:
        return 1