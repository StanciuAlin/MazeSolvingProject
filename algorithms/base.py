from abc import ABC, abstractmethod
import time


class Node:
    """
    Represents a node in the search space.
        Stores the current state, parent for path reconstruction, and costs.
    """

    def __init__(self, position, parent=None, g=0, h=0):
        self.position = position  # (x, y)
        self.parent = parent
        self.g = g  # The cost from start to current node
        self.h = h  # The estimation (heuristic) from current to goal
        self.f = g + h  # The total cost used in A* and Greedy

    def __lt__(self, other):
        # Used by Priority Queue (heapq) in A* and Greedy
        return self.f < other.f


class SearchAlgorithm(ABC):
    """
    Abstract base class for search algorithms.
    """
    @abstractmethod
    def solve(self, maze, start, goal):
        """
        The method that must be implemented by each algorithm.
            Returns a dictionary with results and required metrics.
        """
        pass

    def _reconstruct_path(self, node):
        """
        Rebuild the path from goal back to start using parent references.
        Returns the path as a list of positions from start to goal.
        """
        path = []
        current = node
        while current:
            path.append(current.position)
            current = current.parent
        return path[::-1]  # Invert the path to get it from start to goal
