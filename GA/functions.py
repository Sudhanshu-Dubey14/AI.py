# Import the necessary packages as shown

import random
from deap import base, creator, tools

# Define the evaluation function. It is the first step to create a
# genetic algorithm.

def eval_func(individual):
   target_sum = 15
   return len(individual) - abs(sum(individual) - target_sum),

# Create the toolbox with the right parameters

def create_toolbox(num_bits):
    creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMax)
    toolbox = base.Toolbox() # Initialize the toolbox
    toolbox.register("attr_bool", random.randint, 0, 1)
    toolbox.register("individual", tools.initRepeat, creator.Individual,
    toolbox.attr_bool, num_bits)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    # Register the evaluation operator

    toolbox.register("evaluate", eval_func)

    # Register the crossover operator

    toolbox.register("mate", tools.cxTwoPoint)

    # Register a mutation operator

    toolbox.register("mutate", tools.mutFlipBit, indpb = 0.05)

    # Define the operator for breeding

    toolbox.register("select", tools.selTournament, tournsize = 3)
    return toolbox

