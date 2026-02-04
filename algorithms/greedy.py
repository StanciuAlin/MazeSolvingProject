import heapq
import time
import math
from .base import InformedSearchAlgorithm, Node


class Greedy(InformedSearchAlgorithm):
    def solve(self, maze, start, goal):
        start_time = time.perf_counter()
        expanded_nodes = 0

        # Priority Queue based on only h(n)
        open_list = []
        h_start = self._get_h(start, goal)
        # Set f = h so that heapq sorts by heuristic only
        heapq.heappush(open_list, (h_start, Node(start, h=h_start)))
        visited = {start}

        while open_list:
            _, current_node = heapq.heappop(open_list)
            expanded_nodes += 1

            if current_node.position == goal:
                return self._reconstruct_metrics(
                    current_node, expanded_nodes, start_time,
                    is_optimal=False, visited_list=list(visited))

            for neighbor_pos in maze.get_neighbors(current_node.position):
                if neighbor_pos not in visited:
                    visited.add(neighbor_pos)
                    h = self._get_h(neighbor_pos, goal)
                    heapq.heappush(
                        open_list, (h, Node(neighbor_pos, current_node, h=h)))

        return {
            "algorithm": f"Greedy ({self.heuristic_type})",
            "path": [],
            "expanded_nodes": expanded_nodes,
            "solution_depth": 0,
            "execution_time": time.perf_counter() - start_time,
            "is_optimal": False,
            "visited_list": list(visited)
        }

    def _reconstruct_metrics(self, node, expanded, start_time, is_optimal, visited_list):
        path = self._reconstruct_path(node)
        return {
            "algorithm": f"Greedy ({self.heuristic_type})",
            "path": path,
            "expanded_nodes": expanded,
            "solution_depth": len(path) - 1,
            "execution_time": time.perf_counter() - start_time,
            "is_optimal": is_optimal,
            "visited_list": visited_list
        }
