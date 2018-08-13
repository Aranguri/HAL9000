import numpy as np
import math
import random
from copy import copy, deepcopy
from agent import Agent

def mutate(agent, mutation_coefficient):
    new_agent = deepcopy(agent)

    for h in range(0, len(agent)):
        for i in range(0, agent[h].shape[0]):
            for j in range(0, agent[h].shape[1]):
                max_change = mutation_coefficient * new_agent[h][i][j]
                change = 2 * (random.random() - 0.5) * max_change
                # Esto de hacer que el cambio solo se haga si no se va del rango
                # es vomitivo. Mejorar.
                new_value = new_agent[h][i, j] + change
                if new_value < 1 and new_value > -1 :
                    new_agent[h][i, j] = new_agent[h][i, j] + change

    return Agent(new_agent)

def select(population, killing_coefficient):
    scored_population = sorted([(agent.score, agent) for agent in population], key=lambda x: x[0])
    scored_population = [a for _, a in scored_population]

    number_to_kill = math.floor(killing_coefficient * len(scored_population))
    survivors_size = int(len(scored_population) - number_to_kill)
    scored_population = scored_population[-survivors_size:]
    return scored_population

def procreate(population, mutation_coefficient):
    new_population = deepcopy(population)
    max_children_size = 1

    for index, agent in enumerate(population):
        children_size = math.ceil(max_children_size * (float(index + 1) / len(population)))
        for child in range(0, int(children_size)):
            new_population.append(mutate(agent.ws, mutation_coefficient))

    return new_population

def visually_test_mutate():
    agent = make_random_agent()

    print('Parent:', agent)
    print('Close child:', mutate(agent, 0.1))
    print('A-bit-weird child:', mutate(agent, 0.5))
    print('Who_is_this_guy child:', mutate(agent, 0.5))

def visually_test_select():
    population = []

    for i in range(0, 10):
        population.append(make_random_agent())

    print('Original:', population)
    print('Selected:', select(population))
    print('Original size:', len(population))
    print('Selected size:', len(select(population)))

def visually_test_procreate():
    population = []

    for i in range(0, 3):
        population.append(make_random_agent())

    print('Generation 1:', population)
    print('Generation 2:', procreate(population))

def visually_test_make_random_agent():
    print('Random agent:', make_random_agent())

# visually_test_procreate()
