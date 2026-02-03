from maze_engine import Maze
from algorithms.bfs import BFS
from algorithms.dfs import DFS
from algorithms.astar import AStar
from algorithms.greedy import Greedy
from utils.analyzer import Analyzer
from utils.input_handler import InputHandler


def main():
    # Modifică aici pentru a alege testul dorit
    filename = 'inputs/complex.txt'

    try:
        grid = InputHandler.load_from_file(filename)
        # Setăm Start în colțul stânga-sus și Goal în dreapta-jos
        start = (0, 0)
        goal = (len(grid)-1, len(grid[0])-1)

        # Vizualizare și Execuție
        InputHandler.visualize_input(grid, start, goal)

        maze = Maze(grid)
        algos = [BFS(), DFS(), AStar(), Greedy()]

        analyzer = Analyzer(algos, maze, start, goal)
        results = analyzer.run_tests()
        analyzer.plot_comparison()

    except FileNotFoundError:
        print(
            f"Eroare: Fișierul {filename} nu a fost găsit în folderul inputs/.")


if __name__ == "__main__":
    main()
