import matplotlib.pyplot as plt
import numpy as np
from algorithms.base import Colors


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

        if not self.results:
            print("-" * 62)
            print(
                f"\n{Colors.BOLD}{Colors.YELLOW}[WARNING]{Colors.END} Neither algorithm found a solution.\n The graphic analysis was canceled.")
            return

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

    def print_summary_table(self):
        """
        Prints a summary table of results for all algorithms.
        """
        if not self.results:
            return

        print("\n" + "="*90)
        print(f"{Colors.BOLD}{'ALGORITHM':<25} | {'EXP. NODES':<12} | {'DEPTH':<10} | {'TIME (ms)':<12} | {'IS OPTIMAL?'}{Colors.END}")
        print("-" * 90)

        for res in self.results:
            color = Colors.GREEN if res['is_optimal'] else Colors.YELLOW
            optim_text = "YES" if res['is_optimal'] else "NO"
            time_ms = res['execution_time'] * 1000
            print(f"{color}{res['algorithm']:<25}{Colors.END} | {res['expanded_nodes']:<12} | "
                  f"{res['solution_depth']:<10} | {time_ms:<12.4f} | {color}{optim_text}{Colors.END}")

        print("=" * 90 + "\n")
