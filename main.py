import os
from maze_engine import Maze
from algorithms.bfs import BFS
from algorithms.dfs import DFS
from algorithms.astar import AStar
from algorithms.greedy import Greedy
from utils.analyzer import Analyzer
from utils.input_handler import InputHandler


def run_experiment(grid, start, goal):
    """
    Runs all algorithms on the given maze grid and visualizes results.
        1. Visualizes the input maze with start and goal.
        2. Runs all algorithms and collects performance data.
        3. Visualizes the path found by each algorithm.
        4. Plots a comparative performance graph (Expanded Nodes vs Depth).
    """
    InputHandler.visualize_input(grid, start, goal)

    maze = Maze(grid)
    algos = [BFS(), DFS(), AStar(), Greedy()]

    analyzer = Analyzer(algos, maze, start, goal)
    results = analyzer.run_tests()

    # View the path found by each algorithm
    for res in results:
        InputHandler.visualize_result(
            grid, res['path'], None, title=f"Path found by: {res['algorithm']}")

    # Plot comparison graph
    analyzer.plot_comparison()


def main():
    while True:
        print(23 * "=" + " AI MAZE SOLVER " + 23 * "=" + "\n")
        print("1. Manual Input (Grid dimensions, Walls, Start/Target Nodes)")
        print("2. Read from file (Including start/target)")
        print("3. Exit")
        print(62 * "=")

        choice = input("\nChoose an option: ")

        if choice == '1':
            grid, start, goal = InputHandler.get_manual_input()
            if grid:
                run_experiment(grid, start, goal)

        elif choice == '2':
            folder = 'inputs/'
            files = [f for f in os.listdir(folder) if f.endswith('.txt')]
            print("\nAvailable files:")
            for idx, f in enumerate(files):
                print(f"{idx + 1}. {f}")

            f_idx = int(input("\nChoose the file index: ")) - 1
            filename = os.path.join(folder, files[f_idx])

            grid = InputHandler.load_from_file(filename)
            # For option 2, we ask for start/goal after loading the grid
            print("\nEnter start and goal coordinates:")
            sx = int(input("X Start: "))
            sy = int(input("Y Start: "))
            gx = int(input("X Target: "))
            gy = int(input("Y Target: "))

            run_experiment(grid, (sx, sy), (gx, gy))

        elif choice == '3':
            print("Exit ...")
            break
        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()
