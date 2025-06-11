import tkinter as tk
from tkinter import messagebox

class SudokuSolver:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.entries = [[None for _ in range(9)] for _ in range(9)]
        self.create_grid()
        self.create_buttons()

    def create_grid(self):
        for row in range(9):
            for col in range(9):
                entry = tk.Entry(self.root, width=2, font=('Arial', 18), justify='center')
                entry.grid(row=row, column=col, padx=2, pady=2)
                self.entries[row][col] = entry

    def create_buttons(self):
        solve_btn = tk.Button(self.root, text="Solve", command=self.solve)
        solve_btn.grid(row=9, column=0, columnspan=4)

        clear_btn = tk.Button(self.root, text="Clear", command=self.clear_grid)
        clear_btn.grid(row=9, column=5, columnspan=4)

    def get_grid(self):
        grid = []
        for row in self.entries:
            grid_row = []
            for entry in row:
                val = entry.get()
                grid_row.append(int(val) if val.isdigit() else 0)
            grid.append(grid_row)
        return grid

    def set_grid(self, grid):
        for r in range(9):
            for c in range(9):
                self.entries[r][c].delete(0, tk.END)
                if grid[r][c] != 0:
                    self.entries[r][c].insert(0, str(grid[r][c]))

    def is_valid(self, grid, row, col, num):
        for i in range(9):
            if grid[row][i] == num or grid[i][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for r in range(start_row, start_row + 3):
            for c in range(start_col, start_col + 3):
                if grid[r][c] == num:
                    return False
        return True

    def solve_sudoku(self, grid):
        for row in range(9):
            for col in range(9):
                if grid[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid(grid, row, col, num):
                            grid[row][col] = num
                            if self.solve_sudoku(grid):
                                return True
                            grid[row][col] = 0
                    return False
        return True

    def solve(self):
        grid = self.get_grid()
        if self.solve_sudoku(grid):
            self.set_grid(grid)
        else:
            messagebox.showerror("No Solution", "This Sudoku puzzle cannot be solved.")

    def clear_grid(self):
        for row in self.entries:
            for entry in row:
                entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuSolver(root)
    root.mainloop()