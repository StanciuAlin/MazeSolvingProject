from collections import deque
import time
from .base import SearchAlgorithm, Node


class BFS(SearchAlgorithm):
    def solve(self, maze, start_pos, goal_pos):
        start_time = time.perf_counter()
        expanded_nodes = 0

        # (FIFO)
        queue = deque([Node(start_pos)])
        visited = {start_pos}

        while queue:
            current_node = queue.popleft()
            expanded_nodes += 1

            # Check if we reached the goal
            if current_node.position == goal_pos:
                metrics = self._reconstruct_metrics(
                    current_node, expanded_nodes, start_time, is_optimal=True
                )
                return metrics

            # Explore neighbors
            for neighbor_pos in maze.get_neighbors(current_node.position):
                if neighbor_pos not in visited:
                    visited.add(neighbor_pos)
                    queue.append(Node(neighbor_pos, parent=current_node))

        return None  # No solution path found

    def _reconstruct_metrics(self, node, expanded, start_time, is_optimal):
        path = self._reconstruct_path(node)
        return {
            "algorithm": "BFS",
            "path": path,
            "expanded_nodes": expanded,
            "solution_depth": len(path) - 1,
            "execution_time": time.perf_counter() - start_time,
            "is_optimal": is_optimal
        }
