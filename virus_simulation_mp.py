# Lab 6 - Multiprocessing Version (Fallback)
# Group: Dima, Areej, Amelda

import numpy as np
import multiprocessing as mp

def simulate_infection(process_id, population_size, spread_chance, queue):
    np.random.seed(process_id)
    vaccination_rate = np.random.uniform(0.1, 0.5)
    population = np.zeros(population_size, dtype=int)

    # Initial infection
    if process_id == 0:
        infected_indices = np.random.choice(population_size, int(0.1 * population_size), replace=False)
        population[infected_indices] = 1

    def spread_virus(pop):
        new_pop = pop.copy()
        for i in range(len(pop)):
            if pop[i] == 0 and np.random.rand() < spread_chance * (1 - vaccination_rate):
                new_pop[i] = 1
        return new_pop

    for _ in range(10):  # Simulate 10 time steps
        population = spread_virus(population)

    infected = np.sum(population)
    infection_rate = infected / population_size
    queue.put((process_id, infection_rate, vaccination_rate))

if __name__ == '__main__':
    population_size = 100
    spread_chance = 0.3
    num_processes = 3
    queue = mp.Queue()
    processes = []

    for i in range(num_processes):
        p = mp.Process(target=simulate_infection, args=(i, population_size, spread_chance, queue))
        processes.append(p)
        p.start()

    for _ in range(num_processes):
        pid, rate, vac = queue.get()
        print(f"🦠 Process {pid} Infection Rate: {rate:.2f} (Vaccination Rate: {vac:.2f})")

    for p in processes:
        p.join()