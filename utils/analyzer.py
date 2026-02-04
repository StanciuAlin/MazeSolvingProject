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
        """
        Runs all algorithms on the maze and collects results.
        """
        for algo in self.algorithms:
            res = algo.solve(self.maze, self.start, self.goal)
            if res:
                self.results.append(res)
        return self.results

    def plot_comparison(self):
        """
        Generates a comparative bar chart of expanded nodes and solution depth for each algorithm.
        """
        names = [res['algorithm'] for res in self.results]
        expanded = [res['expanded_nodes'] for res in self.results]
        depth = [res['solution_depth'] for res in self.results]

        x = np.arange(len(names))
        width = 0.35

        fig, ax1 = plt.subplots(figsize=(10, 6))

        # The graphic for Expanded Nodes
        rects1 = ax1.bar(x - width/2, expanded, width,
                         label='Expanded Nodes', color='skyblue')
        ax1.set_ylabel('Number of Nodes')
        ax1.set_title('Performance Comparison of Algorithms')
        ax1.set_xticks(x)
        ax1.set_xticklabels(names)
        ax1.legend(loc='upper left')

        # Secondary graphic for Solution Depth
        ax2 = ax1.twinx()
        rects2 = ax2.bar(x + width/2, depth, width,
                         label='Solution Depth', color='orange')
        ax2.set_ylabel('Solution Depth (steps)')
        ax2.legend(loc='upper right')

        plt.tight_layout()
        plt.show()
