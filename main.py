import os
from maze_engine import Maze
from algorithms.bfs import BFS
from algorithms.dfs import DFS
from algorithms.astar import AStar
from algorithms.greedy import Greedy
from algorithms.base import Colors
from utils.analyzer import Analyzer
from utils.input_handler import InputHandler


def select_algorithms():
    """
    Allows the user to select which algorithms to run.
    Returns a list of algorithm instances.
    """

    print(f"\n{Colors.BOLD}--- Select algorithms ---{Colors.END}\n")
    print(f"{Colors.BOLD}1. BFS (Breadth-First Search){Colors.END}")
    print(f"{Colors.BOLD}2. DFS (Depth-First Search){Colors.END}")
    print(f"{Colors.BOLD}3. A* (Manhattan){Colors.END}")
    print(f"{Colors.BOLD}4. A* (Euclidean){Colors.END}")
    print(f"{Colors.BOLD}5. Greedy (Manhattan){Colors.END}")
    print(f"{Colors.BOLD}6. Greedy (Euclidean){Colors.END}")
    print(f"{Colors.BOLD}7. All algorithms{Colors.END}")

    choice = input(
        f"\n{Colors.BOLD}>> Enter the algorithms ids to compare (comma separated string, e.g. 1, 3, 5): {Colors.END}")

    mapping = {
        '1': BFS(),
        '2': DFS(),
        '3': AStar(heuristic_type="manhattan"),
        '4': AStar(heuristic_type="euclidean"),
        '5': Greedy(heuristic_type="manhattan"),
        '6': Greedy(heuristic_type="euclidean")
    }

    selected = []
    if choice.strip() == '7':
        return list(mapping.values())

    for c in choice.split(','):
        c = c.strip()
        if c in mapping:
            selected.append(mapping[c])

    return selected if selected else list(mapping.values())


def run_experiment(grid, start, goal):
    """
    Runs all algorithms on the given maze grid and visualizes results.
        1. Visualizes the input maze with start and goal.
        2. Runs all algorithms and collects performance data.
        3. Visualizes the path found by each algorithm.
        4. Plots a comparative performance graph (Expanded Nodes vs Depth).
    """

    maze = Maze(grid)
    algos = select_algorithms()

    # 1. Visualize the input maze
    InputHandler.visualize_input(grid, start, goal)

    # 2. Run all algorithms and collect results
    analyzer = Analyzer(algos, maze, start, goal)
    results = analyzer.run_tests()

    if not results:
        print("\n" + "-" * 50)
        print(
            f"{Colors.BOLD}{Colors.YELLOW}[WARNING]{Colors.END} Trap detected \n Neither algorithm found a solution! There is no path from START to TARGET.")
        print("-" * 62)
    else:
        # View the path found by each algorithm
        for res in results:
            # Convert time to milliseconds for better readability
            time_ms = res['execution_time'] * 1000
            status = "Path found" if res['path'] else "Path blocked (Trap)"
            title_with_time = f"{res['algorithm']} | {status} | Timelapse: {time_ms:.4f} ms"
            InputHandler.visualize_result(
                grid,
                res['path'],
                res['visited_list'],
                title=title_with_time)

        # 4. Plot comparison graph. The program is stopped until the last window is closed.
        analyzer.plot_comparison()

        # 5. Print results to terminal
        analyzer.print_summary_table()


def get_coordinates(grid, label):
    """
    Prompt user for valid coordinates (x, y) within the grid for a given label.
    """
    while True:
        try:
            print(
                f"\n{Colors.BOLD}--- Set {label} Node Coordinates ---{Colors.END}")
            x = int(input(f"{Colors.BOLD}>> Enter X: {Colors.END} "))
            y = int(input(f"{Colors.BOLD}>> Enter Y:{Colors.END} "))
            if InputHandler.is_valid_point(grid, x, y):
                return (x, y)
        except ValueError:
            print("Error: Please enter valid integer values.")


def main():
    while True:
        print(3 * '\n' + 23 * f"{Colors.BOLD}{Colors.HEADER}={Colors.END}" +
              f"{Colors.BOLD}{Colors.HEADER} AI MAZE SOLVER {Colors.END}" +
              23 * f"{Colors.BOLD}{Colors.HEADER}={Colors.END}" + "\n")
        print(
            f"{Colors.BOLD}1. Manual Input (Grid dimensions, Walls, Start/Target Nodes){Colors.END}")
        print(f"{Colors.BOLD}2. Read from file (Including start/target){Colors.END}")
        print(f"{Colors.BOLD}3. Random Maze Generation{Colors.END}")
        print(f"{Colors.BOLD}{Colors.RED}4. Exit{Colors.END}")
        print(62 * f"{Colors.BOLD}{Colors.HEADER}={Colors.END}")

        choice = input(f"\n{Colors.BOLD}>> Choose an option: {Colors.END}")
        print()

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
                f_idx = int(
                    input(f"\n{Colors.BOLD}>> Choose the file index:{Colors.END} ")) - 1
                filename = os.path.join(folder, files[f_idx])
                grid = InputHandler.load_from_file(filename)

                start = get_coordinates(grid, "START")
                target = get_coordinates(grid, "TARGET")
                run_experiment(grid, start, target)
            except (ValueError, IndexError):
                print("Invalid selection!")

        elif choice == '3':
            try:
                r = int(input(f"{Colors.BOLD}>> Number of rows:{Colors.END} "))
                c = int(
                    input(f"{Colors.BOLD}>> Number of columns:{Colors.END} "))
                prob = float(
                    input(f"{Colors.BOLD}>> Obstacle probability (e.g. 0.2 for 20%):{Colors.END} "))

                grid = InputHandler.generate_random_maze(r, c, prob)

                # Print the generated grid to help user choose positions
                InputHandler.print_grid_to_terminal(grid)

                # Get suggestions for start and goal positions
                suggestions = InputHandler.get_free_points(grid, count=8)
                print(
                    f"{Colors.CYAN}{Colors.BOLD}\nFree points suggestions:{Colors.END} {Colors.BLUE}{suggestions}{Colors.END}")

                # Force start and goal to be paths in case of overlapping
                print(
                    f"\n{Colors.BOLD}Set the START and TARGET positions:{Colors.END}")
                start = get_coordinates(grid, "START")
                goal = get_coordinates(grid, "TARGET")

                run_experiment(grid, start, goal)
            except ValueError:
                print(
                    f"{Colors.BOLD}{Colors.RED}[Error]{Colors.END} Please enter valid integer values for dimensions and a float for probability.")

        elif choice == '4':
            print(f"{Colors.BOLD}{Colors.RED}Exit ...{Colors.END}")
            break
        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()
