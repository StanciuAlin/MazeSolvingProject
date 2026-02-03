import matplotlib.pyplot as plt
import numpy as np


class InputHandler:
    @staticmethod
    def load_from_file(filename):
        """Citește un labirint dintr-un fișier text."""
        grid = []
        with open(filename, 'r') as f:
            for line in f:
                # 1 pentru perete (#), 0 pentru drum (.)
                grid.append([1 if char == '#' else 0 for char in line.strip()])
        return grid

    @staticmethod
    def visualize_input(grid, start, goal):
        """Afișează grafic labirintul înainte de procesare[cite: 35, 39]."""
        temp_grid = [row[:] for row in grid]
        sx, sy = start
        gx, gy = goal

        plt.figure(figsize=(6, 6))
        plt.imshow(grid, cmap='binary')  # Alb-negru pentru drum/perete
        plt.plot(sy, sx, 'go', label='Start')  # Verde pentru Start
        plt.plot(gy, gx, 'ro', label='Goal')  # Roșu pentru Goal
        plt.title("Vizualizare Input Labirint")
        plt.legend()
        plt.show()

    @staticmethod
    def visualize_result(grid, path, expanded_nodes_list, title="Rezultat Căutare"):
        """
            Afișează labirintul, nodurile explorate și drumul final.
            """
        plt.figure(figsize=(8, 8))
        # Cream o copie pentru vizualizare
        display_grid = np.array(grid)

        # Desenăm labirintul (0=alb, 1=negru)
        plt.imshow(display_grid, cmap='binary')

        # Marcăm nodurile explorate (opțional, pentru a vedea "efortul" algoritmului)
        if expanded_nodes_list:
            ex_x, ex_y = zip(*expanded_nodes_list)
            plt.scatter(ex_y, ex_x, c='yellow', s=10,
                        label='Explorate', alpha=0.3)

        # Desenăm drumul final
        if path:
            px, py = zip(*path)
            plt.plot(py, px, color='red', linewidth=3, label='Calea găsită')

        plt.title(title)
        plt.legend()
        plt.show()
