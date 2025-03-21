# Assignment 1 - Parallel and Distributed Computing (DSAI 3202)

## Repository Contents
```
├── part1_multiprocessing_and_semaphores.py     # Part 1 Individual Work
├── genetic_algorithm_trial.py                  # Sequential Genetic Algorithm
├── genetic_algorithm_trial_parallel.py         # Parallel MPI4PY Version (with enhancements and debugging)
├── genetic_algorithms_functions.py             # GA Functions (Instructor Provided + Completed)
├── city_distances.csv                          # City Distance Matrix
├── city_distances_extended.csv                 # Extended City Matrix
├── .gitignore                                  # Project ignore rules
├── hostfile                                    # MPI Host Configuration
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
- Simulated semaphore-based database access using ConnectionPool.

### 📊 Performance Results:
#### 10⁶ Numbers:
- Sequential Time: ~0.00s
- Pool Map Time: ~0.10s
- Pool Apply Async Time: ~0.14s
- ProcessPoolExecutor Time: ~0.18s

#### 10⁷ Numbers:
- Sequential Time: ~0.79s
- Pool Map Time: ~1.24s
- Pool Apply Async Time: ~520s (Process was killed)

🔸 **Note:** The instructor required apply_async for comparison. The process was killed due to memory and task overhead at large scale — this is expected and highlights limitations of `apply_async()` for large datasets.

---

## 🔸 Part 2: Genetic Algorithm (Group Work)
- Filled missing functions: calculate_fitness and select_in_tournament.
- Explained GA execution flow.
- Proposed MPI4PY parallel design.
- Enhanced version with **adaptive mutation rate** and **elitism**.
- Extended dataset tested successfully.
- Group IPs used for distributed execution.

### 💻 MPI Execution Command
```
/usr/bin/mpirun -np 3 python3 genetic_algorithm_trial_parallel.py
```
> 📌 Runs GA in parallel using 3 processes on a single machine. To run across machines, use a hostfile and proper SSH setup.

---

## 📈 Performance Metrics
- Parallel execution reduced runtime by distributing fitness evaluations.
- Best score improved through elitism and adaptive mutation.

---

## 🏆 Bonus Strategy Implementation

### ✅ Fastest Speedup (5%)
- Used **MPI4PY** to parallelize **fitness calculations** across multiple processes/machines.
- Execution time tracked and benchmarked.

### ✅ Best Score (5%)
- Implemented **Elitism** to preserve top individuals.
- Introduced **Adaptive Mutation Rate** decreasing over time.

### ✅ Both Achieved (15%)
- Combined execution performance and solution quality improvements.

### ✅ AWS Execution (5%)
- Code supports running on AWS EC2 cluster.
- Use the same mpirun command with configured EC2 IPs.

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

---

## 📄 License
Open for educational use only.
