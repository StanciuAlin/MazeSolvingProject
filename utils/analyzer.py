import matplotlib.pyplot as plt
import numpy as np


class Analyzer:
    def __init__(self, algorithms, maze, start, goal):
        self.algorithms = algorithms
        self.maze = maze
        self.start = start
        self.goal = goal
        self.results = []

    def run_tests(self):
        """Rulează toți algoritmii și colectează datele."""
        for algo in self.algorithms:
            res = algo.solve(self.maze, self.start, self.goal)
            if res:
                self.results.append(res)
        return self.results

    def plot_comparison(self):
        """Generează graficele cerute în cerințe."""
        names = [res['algorithm'] for res in self.results]
        expanded = [res['expanded_nodes'] for res in self.results]
        depth = [res['solution_depth'] for res in self.results]

        x = np.arange(len(names))
        width = 0.35

        fig, ax1 = plt.subplots(figsize=(10, 6))

        # Grafic pentru Noduri Expandate
        rects1 = ax1.bar(x - width/2, expanded, width,
                         label='Noduri Expandate', color='skyblue')
        ax1.set_ylabel('Număr Noduri')
        ax1.set_title('Comparație Performanță Algoritmi')
        ax1.set_xticks(x)
        ax1.set_xticklabels(names)
        ax1.legend(loc='upper left')

        # Grafic secundar pentru Adâncimea Soluției
        ax2 = ax1.twinx()
        rects2 = ax2.bar(x + width/2, depth, width,
                         label='Adâncime Soluție', color='orange')
        ax2.set_ylabel('Adâncime (pași)')
        ax2.legend(loc='upper right')

        plt.tight_layout()
        plt.show()
