import matplotlib.pyplot as plt
import numpy as np
from typing import Dict


def plot(histories: dict) -> None:
    fitness = _compute_fitness_per_run(histories)
    fitness_mean = _compute_mean_fitness_per_algorithm(fitness)
    _plot_convergence(fitness_mean)


def _compute_fitness_per_run(histories_dict: dict) -> dict:
    fitness_dict: Dict[str, list] = {}
    for key, histories in histories_dict.items():
        fitness_dict[key] = []
        for history in histories:
            fitness = []
            for generation in history:
                best_fitness = max([solution.f1 for solution in generation])
                fitness.append(best_fitness)
            fitness_dict[key].append(fitness)
    return fitness_dict


def _compute_mean_fitness_per_algorithm(fitness_dict: dict) -> dict:
    mean_fitness_dict: Dict[str, list] = {}
    for key, history in fitness_dict.items():
        mean_fitness_dict[key] = []
        for i in range(len(history[0])):
            mean_fitness = np.mean([history[j][i] for j in range(len(history))])
            mean_fitness_dict[key].append(mean_fitness)
    return mean_fitness_dict


def _plot_convergence(mean: dict) -> None:
    plt.figure(figsize=(16, 6))
    for key in mean.keys():
        plt.plot(mean[key], label=key, linewidth=3)
    plt.legend(loc="upper left", prop={"size": 12})
    plt.ylabel("F1", size=14, labelpad=10)
    plt.xlabel("Generation", size=14, labelpad=10)
    plt.grid(True)
    plt.show()
