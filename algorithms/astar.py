import heapq
import time
import math
from .base import InformedSearchAlgorithm, Node


class AStar(InformedSearchAlgorithm):
    def solve(self, maze, start, goal):
        start_time = time.perf_counter()
        expanded_nodes = 0

        # Priority Queue
        open_list = []
        start_node = Node(start, None, g=0,
                          h=self._get_h(start, goal))
        heapq.heappush(open_list, start_node)

        # Dict to track the lowest g cost found for each position
        visited_costs = {start: 0}

        while open_list:
            current_node = heapq.heappop(open_list)
            expanded_nodes += 1

            if current_node.position == goal:
                return self._reconstruct_metrics(
                    current_node, expanded_nodes, start_time, is_optimal=True,
                    visited_list=list(visited_costs.keys()))

            for neighbor_pos in maze.get_neighbors(current_node.position):
                # The cost from start to neighbor is parent's cost + 1
                new_g = current_node.g + 1

                if neighbor_pos not in visited_costs or new_g < visited_costs[neighbor_pos]:
                    visited_costs[neighbor_pos] = new_g
                    h = self._get_h(neighbor_pos, goal)
                    neighbor_node = Node(
                        neighbor_pos, current_node, g=new_g, h=h)
                    heapq.heappush(open_list, neighbor_node)

        # The case when no path is found
        return {
            "algorithm": f"A* ({self.heuristic_type})",
            "path": [],
            "expanded_nodes": expanded_nodes,
            "solution_depth": 0,
            "execution_time": time.perf_counter() - start_time,
            "is_optimal": False,
            # Returns the explored nodes until failure
            "visited_list": list(visited_costs.keys())
        }

    def _reconstruct_metrics(self, node, expanded, start_time, is_optimal, visited_list):
        path = self._reconstruct_path(node)
        return {
            "algorithm": f"A* ({self.heuristic_type})",
            "path": path,
            "expanded_nodes": expanded,
            "solution_depth": len(path) - 1,
            "execution_time": time.perf_counter() - start_time,
            "is_optimal": is_optimal,
            "visited_list": visited_list
        }
