class Maze:
    def __init__(self, grid):
        """
        Grid: List[List[int]]
            0 is path, 1 is wall
        """
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

    def is_valid_move(self, position):
        """
        Check if a position is within matrix bounds and not a wall.
        """
        x, y = position
        return (0 <= x < self.rows and
                0 <= y < self.cols and
                self.grid[x][y] == 0)

    def get_neighbors(self, position):
        """
        Return a list of valid neighboring positions. (Up, Down, Left, Right)
        """
        x, y = position
        neighbors = []
        # Directions:   Up,      Down,   Left,    Right
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_pos = (x + dx, y + dy)
            if self.is_valid_move(new_pos):
                neighbors.append(new_pos)
        return neighbors
