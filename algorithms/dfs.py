import time
from .base import UninformedSearchAlgorithm, Node


class DFS(UninformedSearchAlgorithm):
    def solve(self, maze, start, goal):
        start_time = time.perf_counter()
        expanded_nodes = 0

        # (LIFO)
        stack = [Node(start)]
        visited = {start}

        while stack:
            current_node = stack.pop()
            expanded_nodes += 1

            if current_node.position == goal:
                return self._reconstruct_metrics(
                    current_node, expanded_nodes, start_time,
                    is_optimal=False, visited_list=list(visited))

            for neighbor_pos in maze.get_neighbors(current_node.position):
                if neighbor_pos not in visited:
                    visited.add(neighbor_pos)
                    stack.append(Node(neighbor_pos, parent=current_node))

        return {
            "algorithm": "DFS",
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
            "algorithm": "DFS",
            "path": path,
            "expanded_nodes": expanded,
            "solution_depth": len(path) - 1,
            "execution_time": time.perf_counter() - start_time,
            "is_optimal": is_optimal,
            "visited_list": visited_list
        }
