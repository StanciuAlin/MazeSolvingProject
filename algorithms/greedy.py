import heapq
import time
from .base import SearchAlgorithm, Node


class Greedy(SearchAlgorithm):
    def _get_h(self, pos, goal_pos):
        return abs(pos[0] - goal_pos[0]) + abs(pos[1] - goal_pos[1])

    def solve(self, maze, start_pos, goal_pos):
        start_time = time.perf_counter()
        expanded_nodes = 0

        # Priority Queue based on only h(n)
        open_list = []
        h_start = self._get_h(start_pos, goal_pos)
        # Set f = h so that heapq sorts by heuristic only
        heapq.heappush(open_list, (h_start, Node(start_pos, h=h_start)))
        visited = {start_pos}

        while open_list:
            _, current_node = heapq.heappop(open_list)
            expanded_nodes += 1

            if current_node.position == goal_pos:
                return self._reconstruct_metrics(
                    current_node, expanded_nodes, start_time, is_optimal=False
                )

            for neighbor_pos in maze.get_neighbors(current_node.position):
                if neighbor_pos not in visited:
                    visited.add(neighbor_pos)
                    h = self._get_h(neighbor_pos, goal_pos)
                    heapq.heappush(
                        open_list, (h, Node(neighbor_pos, current_node, h=h)))

        return None

    def _reconstruct_metrics(self, node, expanded, start_time, is_optimal):
        path = self._reconstruct_path(node)
        return {
            "algorithm": "Greedy",
            "path": path,
            "expanded_nodes": expanded,
            "solution_depth": len(path) - 1,
            "execution_time": time.perf_counter() - start_time,
            "is_optimal": is_optimal
        }
