# genetic_algorithm_trial_parallel.py
# MPI4PY Version of Genetic Algorithm with Enhancements and Debugging
# Group: Dima, Areej, Amelda

from mpi4py import MPI
import numpy as np
import pandas as pd
import time
from genetic_algorithms_functions import calculate_fitness, \
    select_in_tournament, order_crossover, mutate, generate_unique_population

# MPI Setup
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Load distance matrix
distance_matrix = pd.read_csv('city_distances.csv').to_numpy()
num_nodes = distance_matrix.shape[0]

# DEBUG: Print a sample of distance matrix to verify it's loaded correctly
if rank == 0:
    print("\n[DEBUG] Distance Matrix Sample (top-left 5x5):")
    print(distance_matrix[:5, :5])

# Parameters
population_size = 10000
mutation_rate = 0.1
num_generations = 200
stagnation_limit = 5
elitism_size = 5

# Master Process initializes population
if rank == 0:
    np.random.seed(42)
    population = generate_unique_population(population_size, num_nodes)
else:
    population = None

# Broadcast initial population
population = comm.bcast(population, root=0)

# Track runtime
if rank == 0:
    total_start = time.time()

# Genetic Algorithm Loop
best_fitness = int(1e6)
stagnation_counter = 0

for generation in range(num_generations):
    # Divide population chunk to each worker
    chunk_size = len(population) // size
    start_idx = rank * chunk_size
    end_idx = len(population) if rank == size - 1 else (rank + 1) * chunk_size
    local_population = population[start_idx:end_idx]

    # Each process computes fitness for its chunk
    local_scores = [calculate_fitness(route, distance_matrix) for route in local_population]

    # Gather all scores at root
    all_scores = comm.gather(local_scores, root=0)

    if rank == 0:
        # Flatten all scores
        flat_scores = [score for sublist in all_scores for score in sublist]

        # Check stagnation
        current_best_fitness = np.min(flat_scores)
        if current_best_fitness < best_fitness:
            best_fitness = current_best_fitness
            stagnation_counter = 0
        else:
            stagnation_counter += 1

        # Regenerate population if stagnation occurs
        if stagnation_counter >= stagnation_limit:
            print(f"[GEN {generation}] Stagnation detected. Regenerating population...")
            best_individual = population[np.argmin(flat_scores)]
            population = generate_unique_population(population_size - 1, num_nodes)
            population.append(best_individual)
            stagnation_counter = 0
            continue

        # Sort by fitness (best first)
        sorted_indices = np.argsort(flat_scores)
        best_individuals = [population[i] for i in sorted_indices[:elitism_size]]

        # Selection, crossover, mutation
        selected = select_in_tournament(population, np.array(flat_scores))
        offspring = []
        for i in range(0, len(selected) - 1, 2):
            parent1, parent2 = selected[i], selected[i + 1]
            route1 = order_crossover(parent1[1:], parent2[1:])
            offspring.append([0] + route1)

        # Adaptive mutation rate
        adaptive_mutation_rate = mutation_rate * (1 - (generation / num_generations))
        mutated_offspring = [mutate(route, adaptive_mutation_rate) for route in offspring]

        # Replace worst individuals with new offspring and elitism
        replace_indices = sorted_indices[::-1][:len(mutated_offspring)]
        for i, idx in enumerate(replace_indices):
            population[idx] = mutated_offspring[i]

        # Inject elitism
        for i in range(elitism_size):
            population[i] = best_individuals[i]

        # Ensure uniqueness
        unique_population = set(tuple(ind) for ind in population)
        while len(unique_population) < population_size:
            individual = [0] + list(np.random.permutation(np.arange(1, num_nodes)))
            unique_population.add(tuple(individual))
        population = [list(ind) for ind in unique_population]

        print(f"[GEN {generation}] Best Fitness = {current_best_fitness:.2f}")

    # Broadcast updated population
    population = comm.bcast(population, root=0)

# Final evaluation and runtime tracking
if rank == 0:
    final_scores = [calculate_fitness(route, distance_matrix) for route in population]
    best_idx = np.argmin(final_scores)
    total_time = time.time() - total_start

    print("\nBest Solution Route:", population[best_idx])
    print("Total Distance:", -final_scores[best_idx])
    print("Total Execution Time (Parallel):", round(total_time, 2), "seconds")

    # Additional Debug Print (Safe - non-invasive)
    print("\n[DEBUG] Final Best Route:", population[best_idx])
    print("[DEBUG] Final Best Distance (should be negative):", calculate_fitness(population[best_idx], distance_matrix))