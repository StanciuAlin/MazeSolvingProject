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


def get_coordinates(grid, label):
    """
    Prompt user for valid coordinates (x, y) within the grid for a given label.
    """
    while True:
        try:
            print(f"\n--- Config/Set {label} ---")
            x = int(input(f"Enter X {label}: "))
            y = int(input(f"Enter Y {label}: "))
            if InputHandler.is_valid_point(grid, x, y):
                return (x, y)
        except ValueError:
            print("Error: Please enter valid integer values.")


def main():
    while True:
        print(23 * "=" + " AI MAZE SOLVER " + 23 * "=" + "\n")
        print("1. Manual Input (Grid dimensions, Walls, Start/Target Nodes)")
        print("2. Read from file (Including start/target)")
        print("3. Random Maze Generation")
        print("3. Exit")
        print(62 * "=")

        choice = input("\nChoose an option: ")

        if choice == '1':
            grid, _, _ = InputHandler.get_manual_input()
            if grid:
                start = get_coordinates(grid, "START")
                target = get_coordinates(grid, "TARGET")
                run_experiment(grid, start, target)

        elif choice == '2':
            folder = 'inputs/'
            files = [f for f in os.listdir(folder) if f.endswith('.txt')]
            if not files:
                print("No file found in inputs folder!")
                continue

            print("\nAvailable files:")
            for idx, f in enumerate(files):
                print(f"{idx + 1}. {f}")

            try:
                f_idx = int(input("\nChoose the file index: ")) - 1
                filename = os.path.join(folder, files[f_idx])
                grid = InputHandler.load_from_file(filename)

                start = get_coordinates(grid, "START")
                target = get_coordinates(grid, "TARGET")
                run_experiment(grid, start, target)
            except (ValueError, IndexError):
                print("Invalid selection!")

        elif choice == '3':
            try:
                r = int(input("Number of rows: "))
                c = int(input("Number of columns: "))
                prob = float(
                    input("Obstacle probability (e.g. 0.2 for 20%): "))

                grid = InputHandler.generate_random_maze(r, c, prob)

                # Force start and goal to be paths in case of overlapping
                print("\nSet the START and TARGET positions:")
                start = get_coordinates(grid, "START")
                goal = get_coordinates(grid, "TARGET")

                run_experiment(grid, start, goal)
            except ValueError:
                print(
                    "Error: Please enter valid integer values for dimensions and a float for probability.")

        elif choice == '4':
            print("Exit ...")
            break
        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()
