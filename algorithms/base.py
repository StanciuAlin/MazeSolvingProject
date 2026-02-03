from abc import ABC, abstractmethod
import time

class Node:
    """
    Reprezintă un nod în spațiul de căutare.
    Stochează starea curentă, părintele pentru reconstrucția drumului și costurile.
    """
    def __init__(self, position, parent=None, g=0, h=0):
        self.position = position  # (x, y)
        self.parent = parent
        self.g = g  # Costul de la start la nodul curent
        self.h = h  # Estimarea (euristica) până la țintă
        self.f = g + h  # Costul total (folosit în A*)

    def __lt__(self, other):
        # Necesar pentru Priority Queue (heapq) în A* și Greedy
        return self.f < other.f

class SearchAlgorithm(ABC):
    """
    Interfață abstractă pentru algoritmii de căutare (Open/Closed Principle).
    """
    @abstractmethod
    def solve(self, maze, start, goal):
        """
        Metodă ce trebuie implementată de fiecare algoritm.
        Returnează un dicționar cu rezultatele și metricile cerute.
        """
        pass

    def _reconstruct_path(self, node):
        """
        Reconstruiește drumul de la țintă înapoi la start folosind referințele către părinți.
        """
        path = []
        current = node
        while current:
            path.append(current.position)
            current = current.parent
        return path[::-1] # Inversăm pentru a avea drumul de la Start la Goal