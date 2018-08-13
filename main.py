from agent import Agent
from evolution import select, procreate
import matplotlib.pyplot as plt
import itertools
import numpy as np
import time

pop_size = 12
agents = [Agent() for _ in range(pop_size)]
scores = []

for i in itertools.count():
    for agent in agents: agent.main()
    best_agent = agents[np.argmax([a.score for a in agents])]
    print ('Max score: {}'.format(best_agent.score))
    print ('Best code: {} \n'.format(best_agent.code))
    scores.append(best_agent.score)
    if best_agent.score == 1.0:
        print('finished')
        time.sleep(1000000)

    selected_agents = select(agents, 0.5)
    agents = procreate(selected_agents, 0.5)
    if (i + 1) % 25 == 0:
        plt.plot(scores)
        plt.show(block=False)
        time.sleep(1)
        plt.close()
