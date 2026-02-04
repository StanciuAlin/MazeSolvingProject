import time
from .base import SearchAlgorithm, Node


class DFS(SearchAlgorithm):
    def solve(self, maze, start_pos, goal_pos):
        start_time = time.perf_counter()
        expanded_nodes = 0

        # (LIFO)
        stack = [Node(start_pos)]
        visited = {start_pos}

        while stack:
            current_node = stack.pop()
            expanded_nodes += 1

            if current_node.position == goal_pos:
                return self._reconstruct_metrics(
                    current_node, expanded_nodes, start_time, is_optimal=False
                )

            for neighbor_pos in maze.get_neighbors(current_node.position):
                if neighbor_pos not in visited:
                    visited.add(neighbor_pos)
                    stack.append(Node(neighbor_pos, parent=current_node))

        return None

    def _reconstruct_metrics(self, node, expanded, start_time, is_optimal):
        path = self._reconstruct_path(node)
        return {
            "algorithm": "DFS",
            "path": path,
            "expanded_nodes": expanded,
            "solution_depth": len(path) - 1,
            "execution_time": time.perf_counter() - start_time,
            "is_optimal": is_optimal
        }
