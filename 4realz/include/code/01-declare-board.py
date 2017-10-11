import z3

# Define a 16x16 Sudoku
order = 4
side = order ** 2

# Create a solver
smt = z3.Solver()

cells = [list() for row in range(side)]
for r in range(side):
    for c in range(side):
        cells[r].append(z3.Int('cell_%x%x' % (r, c)))
