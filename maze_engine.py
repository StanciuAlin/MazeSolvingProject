class Maze:
    def __init__(self, grid):
        """
        grid: Matrice (listă de liste) unde 0 = drum, 1 = zid.
        """
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

    def is_valid_move(self, position):
        """
        Verifică dacă o poziție este în interiorul matricii și nu este un zid.
        """
        x, y = position
        return (0 <= x < self.rows and 
                0 <= y < self.cols and 
                self.grid[x][y] == 0)

    def get_neighbors(self, position):
        """
        Returnează vecinii accesibili (Sus, Jos, Stânga, Dreapta).
        """
        x, y = position
        neighbors = []
        # Direcții: Sus, Jos, Stânga, Dreapta
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_pos = (x + dx, y + dy)
            if self.is_valid_move(new_pos):
                neighbors.append(new_pos)
        return neighbors