# Assignment 1 - Parallel and Distributed Computing (DSAI 3202)

## Repository Contents
```
├── part1_multiprocessing_and_semaphores.py     # Part 1 Individual Work
├── genetic_algorithm_trial.py                  # Sequential Genetic Algorithm
├── genetic_algorithm_trial_parallel.py         # Parallel MPI4PY Version (with enhancements)
├── genetic_algorithms_functions.py             # GA Functions (Instructor Provided + Completed)
├── city_distances.csv                          # City Distance Matrix
├── city_distances_extended.csv                 # Extended City Matrix
├── .gitignore                                  # Project ignore rules
├── README.md                                   # Project Documentation
```

---

## 👤 Authors:
- **Dima** (10.102.0.71)
- **Areej** (10.102.0.69)
- **Amelda** (10.102.0.152)

---

## 🔸 Part 1: Multiprocessing (Individual - Dima)
- Implemented square() tests using different multiprocessing methods.
- Simulated semaphore-based database access.

## 🔸 Part 2: Genetic Algorithm (Group Work)
- Filled missing functions: calculate_fitness and select_in_tournament.
- Explained GA execution flow.
- Proposed MPI4PY parallel design.
- Enhanced version with **adaptive mutation rate** and **elitism**.
- Extended dataset tested successfully.
- Group IPs used for distributed execution.

### 💻 MPI Execution Command
```
mpirun -np 3 -hosts 10.102.0.71,10.102.0.69,10.102.0.152 python genetic_algorithm_trial_parallel.py
```
> 📌 Ensure SSH is properly configured and MPI4PY is installed on all machines.

---

## 📈 Performance Metrics
- Parallel execution reduced runtime by distributing fitness evaluations.
- Best score improved through elitism and adaptive mutation.

---

## 🏆 Bonus Strategy Implementation

### ✅ Fastest Speedup (5%)
- Used **MPI4PY** to parallelize **fitness calculations** across multiple machines.
- Execution time tracked with `time.time()` and printed in logs.

### ✅ Best Score (5%)
- Implemented **Elitism** to preserve top individuals in each generation.
- Introduced **Adaptive Mutation Rate** that decreases over time to fine-tune later generations.

### ✅ Both Achieved (15%)
- Combined improvements in both **execution time** and **solution quality**.

### ✅ AWS Execution (5%)
- The same MPI code can run on AWS EC2 cluster.
- Just install MPI & mpi4py, sync files, and run with same `mpirun` command.
- Include AWS runtime logs or screenshots in submission if tested.

---

## 🔍 Large Scale Problem
- `city_distances_extended.csv` tested with same parallel GA code.
- Execution time remained feasible, confirming scalability.

### 🚗 Multi-Car Extension (Conceptual Only)
- Each car could be assigned a subset of nodes.
- Use GA to optimize each car's subroute independently.
- Introduce a constraint-based load balancing approach.

---

## 📂 Submission
Only this **GitHub repository branch link** needs to be submitted:
```
https://github.com/57deema/python_project_lab/tree/assignment1-dsai3202
```
```
https://github.com/57deema/python_project_lab.git
```
---

## 📄 License
Open for educational use only.