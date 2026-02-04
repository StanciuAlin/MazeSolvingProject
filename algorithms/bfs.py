from collections import deque
import time
from .base import UninformedSearchAlgorithm, Node


class BFS(UninformedSearchAlgorithm):
    # Uninformed Search Algorithm - Breadth-First Search

    def solve(self, maze, start, goal):
        start_time = time.perf_counter()
        expanded_nodes = 0

        # (FIFO)
        queue = deque([Node(start)])
        visited = {start}

        while queue:
            current_node = queue.popleft()
            expanded_nodes += 1

            # Check if we reached the goal
            if current_node.position == goal:
                metrics = self._reconstruct_metrics(
                    current_node, expanded_nodes, start_time, is_optimal=True, visited_list=list(visited)
                )
                return metrics

            # Explore neighbors
            for neighbor_pos in maze.get_neighbors(current_node.position):
                if neighbor_pos not in visited:
                    visited.add(neighbor_pos)
                    queue.append(Node(neighbor_pos, parent=current_node))

        # No solution path found
        return {
            "algorithm": "BFS",
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
            "algorithm": "BFS",
            "path": path,
            "expanded_nodes": expanded,
            "solution_depth": len(path) - 1,
            "execution_time": time.perf_counter() - start_time,
            "is_optimal": is_optimal,
            "visited_list": visited_list
        }
