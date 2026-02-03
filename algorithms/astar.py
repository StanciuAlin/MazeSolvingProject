import heapq
import time
from .base import SearchAlgorithm, Node


class AStar(SearchAlgorithm):
    def __init__(self, heuristic_type="manhattan"):
        self.heuristic_type = heuristic_type

    def _get_h(self, pos, goal_pos):
        """Calculează euristica: Distanța Manhattan."""
        return abs(pos[0] - goal_pos[0]) + abs(pos[1] - goal_pos[1])

    def solve(self, maze, start_pos, goal_pos):
        start_time = time.perf_counter()
        expanded_nodes = 0

        # Coada de priorități (Priority Queue)
        open_list = []
        start_node = Node(start_pos, None, g=0,
                          h=self._get_h(start_pos, goal_pos))
        heapq.heappush(open_list, start_node)

        # Dicționar pentru a urmări cel mai mic cost g găsit pentru fiecare poziție
        visited_costs = {start_pos: 0}

        while open_list:
            current_node = heapq.heappop(open_list)
            expanded_nodes += 1

            if current_node.position == goal_pos:
                return self._reconstruct_metrics(
                    current_node, expanded_nodes, start_time, is_optimal=True
                )

            for neighbor_pos in maze.get_neighbors(current_node.position):
                # Costul de la start la vecin este costul părintelui + 1
                new_g = current_node.g + 1

                if neighbor_pos not in visited_costs or new_g < visited_costs[neighbor_pos]:
                    visited_costs[neighbor_pos] = new_g
                    h = self._get_h(neighbor_pos, goal_pos)
                    neighbor_node = Node(
                        neighbor_pos, current_node, g=new_g, h=h)
                    heapq.heappush(open_list, neighbor_node)

        return None

    def _reconstruct_metrics(self, node, expanded, start_time, is_optimal):
        path = self._reconstruct_path(node)
        return {
            "algorithm": "A*",
            "path": path,
            "expanded_nodes": expanded,
            "solution_depth": len(path) - 1,
            "execution_time": time.perf_counter() - start_time,
            "is_optimal": is_optimal
        }
