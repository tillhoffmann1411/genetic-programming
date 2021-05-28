# This script is for running the optimization with multiprocessing
# To use the script you have to change the path in some places

from deap import base, creator, tools, gp, algorithms
import operator, random
from stock import Stock
import numpy as np
from tree_plot import *
from primitive_functions import *
from parser import *
from dateutil.relativedelta import relativedelta
import time
import multiprocessing

path = "/investment_example/"

pset = gp.PrimitiveSetTyped("main", [Stock], int)

# Define primitive functions for the nodes. The first parameter defines the function, the second the types of the input parameters and the third one the type of the output.

pset.addPrimitive(profit10, [Stock, int, int], int, name="profit_larger_10")
pset.addPrimitive(profit20, [Stock, int, int], int, name="profit_larger_20")
pset.addPrimitive(profit30, [Stock, int, int], int, name="profit_larger_30")
pset.addPrimitive(profit40, [Stock, int, int], int, name="profit_larger_40")
pset.addPrimitive(profit50, [Stock, int, int], int, name="profit_larger_50")
pset.addPrimitive(profit60, [Stock, int, int], int, name="profit_larger_60")
pset.addPrimitive(profit70, [Stock, int, int], int, name="profit_larger_70")
pset.addPrimitive(profit80, [Stock, int, int], int, name="profit_larger_80")
pset.addPrimitive(profit90, [Stock, int, int], int, name="profit_larger_90")
pset.addPrimitive(risk10, [Stock, int, int], int, name="risk_larger_10")
pset.addPrimitive(risk20, [Stock, int, int], int, name="risk_larger_20")
pset.addPrimitive(risk30, [Stock, int, int], int, name="risk_larger_30")
pset.addPrimitive(risk40, [Stock, int, int], int, name="risk_larger_40")
pset.addPrimitive(risk50, [Stock, int, int], int, name="risk_larger_50")
pset.addPrimitive(risk60, [Stock, int, int], int, name="risk_larger_60")
pset.addPrimitive(risk70, [Stock, int, int], int, name="risk_larger_70")
pset.addPrimitive(risk80, [Stock, int, int], int, name="risk_larger_80")
pset.addPrimitive(risk90, [Stock, int, int], int, name="risk_larger_90")
pset.addPrimitive(stock, [Stock], Stock, name="asset_f")


pset.addTerminal(0, int)
pset.addTerminal(12, int)
pset.addTerminal(24, int)
pset.addTerminal(48, int)


# Renaming the input parameter

pset.renameArguments(ARG0="asset")


# # 2. Defining Object types
# In any evolutionary program, we need some basic object types. In this case we need two, a fitness type and the type for individuals. In this problem we are facing an maximization and minimization problem (maximize the value and minimize the tree size)(so the one value is positive and the other one is negative). The individual will be based upon a tree, to which we add the defined fitness.


creator.create("Fitness", base.Fitness, weights=(1.0, -1.0, ))
creator.create("Individual", gp.PrimitiveTree, fitness=creator.Fitness, pset=pset)


# # 3. Define helper functions
# Register functions that we during the whole algorithm (generate, evaluate, mutate, ...). Any structure with access to the toolbox will also have access to all of those registered parameters.

# ## 3.1 Generating individuals


toolbox = base.Toolbox()
# Defines how a tree expression looks like
toolbox.register("expr", gp.genHalfAndHalf, pset=pset, min_=1, max_=6)
# How an individual should be generated (in this case as a tree)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr)
# How the population of individuals should look like
toolbox.register("population", tools.initRepeat, list, toolbox.individual)


# ## 3.2 Evaluation
# Define functions that help us to evaluate an individuum. This includes to calculate the fitness. But first we need to generate executable pythoncode out of our tree individuals.
# 
# To get working python code out of our generated tree we can use the `gp.compile` function.


nr_samples = 25
# Parse stocks
all_symbols = load_nasdaq_symbols(top=nr_samples)
all_assets = generate_all_assets(all_symbols, sample=nr_samples)



# Generates Python code out of trees
toolbox.register("compile", gp.compile, pset=pset)

def evaluate(tree):
    # using the previously defined compile function
    function = toolbox.compile(tree)

    # Set end date which is used to generate the trees
    end = datetime(2015, 1, 23)

    # Following part is used to evaluate the trees
    profit = 0.0
    risk = 0.0
    # Go through some sample assets and get a recommendation for how long one should hold the stock, based on the historical data
    for asset in all_assets:
        hold_duration = function(asset)

        if hold_duration is not None and hold_duration > 0:
            # Get the profit and risk for the calculated hold time for one specific asset
            future_profit = asset.get_avg_profit(start=end, end=end + relativedelta(months=hold_duration))
            future_risk = asset.get_avg_risk(start=end, end=end + relativedelta(months=hold_duration))
            profit += future_profit
            risk += future_risk

    profit = profit / nr_samples
    risk = risk / nr_samples
    return profit, risk,

# Now add the evaluation Function to our toolbox
toolbox.register("evaluate", evaluate)


# ## 3.3 Selection for next generation
# Select the best individual among tournsize randomly chosen individuals, k times. The list returned contains references to the input individuals.


toolbox.register("select", tools.selTournament, tournsize=2)


# ## 3.4 Reproduction
# Define random mutations for individuals.
# 
# Mutation strategy: Randomly select a point in the tree individual, then replace the subtree at that point as a root by the expression generated using method expr_mut().
# 
# Crossover strategy: Randomly select crossover point in each individual and exchange each subtree with the point as root between each individual.


# Defines how the expression of a tree mutation should look like
toolbox.register("expr_mut", gp.genFull, min_=0, max_=2)
# How the mutation should be applied
toolbox.register("mutate", gp.mutUniform, expr=toolbox.expr_mut, pset=pset)

# Crossover
toolbox.register("mate", gp.cxOnePoint)


# Limit the height of individual to avoid bloat
toolbox.decorate("mutate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17))
toolbox.decorate("mate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17))


# # 4. Add some statistics
#  In this case, we want to compute the mean, standard deviation, minimum, and maximum of both the individuals fitness and size.

avg_size = pd.DataFrame()
avg_profit = pd.DataFrame()
avg_risk = pd.DataFrame()

def stats():
    stats_profit = tools.Statistics(lambda ind: ind.fitness.values[0])
    stats_risk = tools.Statistics(lambda ind: ind.fitness.values[1])
    stats_size = tools.Statistics(len)
    mstats = tools.MultiStatistics(profit=stats_profit, risk=stats_risk, size=stats_size)
    mstats.register("avg", np.mean)
    mstats.register("min", np.min)
    mstats.register("max", np.max)
    return mstats


# 5. Plott trees
def plot(trees, name_pre = ""):
    write_file(trees[0])
    for index, tree in zip(range(len(trees)), trees):
        # Generate Graph
        print("generate Graph for tree " + str(index))
        nodes, edges, labels = gp.graph(tree)
        plot_tree(nodes, edges, labels, "tree_" + name_pre + "_" + str(index))




def run_gp(i: int):
    pop = toolbox.population(n=10)
    hof = tools.HallOfFame(1)

    mstats = stats()

    pop, log = algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=200, halloffame=hof, stats=mstats, verbose=True)

    plot(hof, name_pre=str(i))

    avg_size[i] = log.chapters["size"].select("avg")
    avg_profit[i] = log.chapters["profit"].select("avg")
    avg_risk[i] = log.chapters["risk"].select("avg")

if __name__ == '__main__':
  pool = multiprocessing.Pool()
  toolbox.register("map", pool.map)

  run_n_times = 10


  starttime = time.time()

  for i in range(run_n_times):
   run_gp(i)
   print('Time for step {}: {} seconds'.format(i, time.time() - starttime))

  print()
  print('Time taken = {} seconds'.format(time.time() - starttime))

  chart_all_size = avg_size.plot().get_figure()
  chart_all_profit = avg_profit.plot().get_figure()
  chart_all_risk = avg_risk.plot().get_figure()

  avg_size['avg'] = avg_size.mean(axis=1)
  avg_profit['avg'] = avg_profit.mean(axis=1)
  avg_risk['avg'] = avg_risk.mean(axis=1)

  avg_size.to_csv(path + 'results/size.csv')
  avg_profit.to_csv(path + 'results/profit.csv')
  avg_risk.to_csv(path + 'results/risk.csv')

  chart_avg_size = avg_size.iloc[:,-1:].plot(ylabel="tree size").get_figure()
  chart_avg_profit = avg_profit.iloc[:,-1:].plot(ylabel="profit").get_figure()
  chart_avg_risk = avg_risk.iloc[:,-1:].plot(ylabel="risk").get_figure()

  chart_all_size.savefig(path + "images/chart_all_size.png")
  chart_all_profit.savefig(path + "images/chart_all_profit.png")
  chart_all_risk.savefig(path + "images/chart_all_risk.png")

  chart_avg_size.savefig(path + "images/chart_avg_size.png")
  chart_avg_profit.savefig(path + "images/chart_avg_profit.png")
  chart_avg_risk.savefig(path + "images/chart_avg_risk.png")

