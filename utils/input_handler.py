import matplotlib.pyplot as plt
import numpy as np


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
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))

            print("Enter the grid (use '.' for path and '#' for walls):")
            grid = []
            for i in range(rows):
                row_str = input(f"Row {i}: ").strip()
                while len(row_str) != cols:
                    print(
                        f"Error: Row must have exactly {cols} characters.")
                    row_str = input(f"Row {i}: ").strip()
                grid.append([1 if char == '#' else 0 for char in row_str])

            start_x = int(input("X Start: "))
            start_y = int(input("Y Start: "))
            goal_x = int(input("X Target: "))
            goal_y = int(input("Y Target: "))

            return grid, (start_x, start_y), (goal_x, goal_y)
        except ValueError:
            print("Error: Please enter valid integer values.")
            return None, None, None

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
            plt.scatter(ex_y, ex_x, c='yellow', s=10,
                        label='Explored', alpha=0.3)

        if path:
            px, py = zip(*path)
            plt.plot(py, px, color='red', linewidth=3, label='The path found')

        plt.title(title)
        plt.legend()
        plt.show()
