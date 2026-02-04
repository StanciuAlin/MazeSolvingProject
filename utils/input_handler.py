import matplotlib.pyplot as plt
import numpy as np
import random
from algorithms.base import Colors


class InputHandler:
    @staticmethod
    def load_from_file(filename):
        """
            Read maze grid from a text file. Each line in the file represents a row in the maze.
            Walls are represented by '#' and paths by '.'.
            1 is used for walls and 0 for paths in the returned grid.
        """
        grid = []
        with open(filename, 'r') as f:
            for line in f:
                # 1 for wall, 0 for path
                grid.append([1 if char == '#' else 0 for char in line.strip()])
        return grid

    @staticmethod
    def get_manual_input():
        """
        Allow the user to manually input the maze grid, start, and goal positions.
        """
        try:
            rows = int(
                input(f"{Colors.BOLD}>> Enter number of rows:{Colors.END} "))
            cols = int(
                input(f"{Colors.BOLD}>> Enter number of columns:{Colors.END} "))

            print(
                f"{Colors.BOLD}Enter the grid (use '.' for path and '#' for walls):{Colors.END}")
            grid = []
            for i in range(rows):
                row_str = input(
                    f"{Colors.BOLD}>> Row {i}:{Colors.END} ").strip()
                while len(row_str) != cols:
                    print(
                        f"{Colors.RED}{Colors.BOLD}[Error]{Colors.END} Row must have exactly {cols} characters.")
                    row_str = input(
                        f"{Colors.BOLD}>> Row {i}:{Colors.END} ").strip()
                grid.append([1 if char == '#' else 0 for char in row_str])

            start_x = int(input(f"{Colors.BOLD}>> X Start:{Colors.END} "))
            start_y = int(input(f"{Colors.BOLD}>> Y Start:{Colors.END} "))
            goal_x = int(input(f"{Colors.BOLD}>> X Target:{Colors.END} "))
            goal_y = int(input(f"{Colors.BOLD}>> Y Target:{Colors.END} "))

            return grid, (start_x, start_y), (goal_x, goal_y)
        except ValueError:
            print(
                f"{Colors.RED}{Colors.BOLD}[Error]{Colors.END} Please enter valid integer values.")
            return None, None, None

    @staticmethod
    def is_valid_point(grid, x, y):
        """
        Check if the point (x, y) is within the grid bounds and not a wall.
        """
        rows = len(grid)
        cols = len(grid[0])
        if 0 <= x < rows and 0 <= y < cols:
            if grid[x][y] == 0:
                return True
            else:
                print(
                    f"{Colors.RED}{Colors.BOLD}[Error]{Colors.END} Position ({x}, {y}) is a WALL (#).")
                return False
        print(
            f"{Colors.RED}{Colors.BOLD}[Error]{Colors.END} Position ({x}, {y}) is out of bounds ({rows}x{cols}).")
        return False

    @staticmethod
    def generate_random_maze(rows, cols, obstacle_prob=0.25):
        """
        Generate a random maze grid of given dimensions. Each cell has a probability of being an obstacle (wall).
        """
        grid = [[1 if random.random() < obstacle_prob else 0 for _ in range(cols)]
                for _ in range(rows)]
        return grid

    @staticmethod
    def get_free_points(grid, count=5):
        """
        Return a list of free (path) points in the grid.
        """
        free_points = []
        for r, row in enumerate(grid):
            for c, value in enumerate(row):
                if value == 0:
                    free_points.append((r, c))

        # Return a random sample of free points if there are enough
        import random
        return random.sample(free_points, min(len(free_points), count))

    @staticmethod
    def print_grid_to_terminal(grid):
        """
            Print the maze grid to the terminal (as a preview).
        """
        print(f"\n{Colors.BOLD}Maze Preview ( . = Path, # = Wall):\n{Colors.END}")
        header = "   " + "".join([str(i % 10) for i in range(len(grid[0]))])
        print(header)
        for i, row in enumerate(grid):
            row_str = "".join(['.' if cell == 0 else '#' for cell in row])
            print(f"{i:<3}{row_str}")

    @staticmethod
    def visualize_input(grid, start, goal):
        """
            Display the maze grid with start and goal positions marked.
        """
        temp_grid = [row[:] for row in grid]
        sx, sy = start
        gx, gy = goal

        plt.figure(figsize=(6, 6))
        plt.imshow(grid, cmap='binary')  # 0=white (path), 1=black (wall)
        plt.plot(sy, sx, 'go', label='Start')
        plt.plot(gy, gx, 'ro', label='Goal')
        plt.title("View Input Maze")
        plt.legend()
        plt.show()

    @staticmethod
    def visualize_result(grid, path, expanded_nodes_list, title="Rezultat Căutare"):
        """
            Display the maze, the path found, and the expanded nodes.           
        """

        plt.figure(figsize=(8, 8))
        display_grid = np.array(grid)

        plt.imshow(display_grid, cmap='binary')

        if expanded_nodes_list:
            ex_x, ex_y = zip(*expanded_nodes_list)
            plt.scatter(ex_y, ex_x, c='lime', s=15,
                        label='Explored', alpha=0.5)

        if path and len(path) > 0:
            px, py = zip(*path)
            plt.plot(py, px, color='red', linewidth=3, label='The path found')
        else:
            # Show "PATH NOT FOUND" message in the center of the maze
            plt.text(len(grid[0])//2, len(grid)//2, "PATH NOT FOUND",
                     color="red", fontsize=20, fontweight="bold",
                     ha="center", va="center", bbox=dict(facecolor='white', alpha=0.7))

        plt.title(title)
        plt.legend()
        plt.show()
