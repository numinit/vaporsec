import z3

# Define a 16x16 Sudoku
order = 4; side = order ** 2

# Create a solver and a 16x16 board (list of lists)
smt = z3.Solver()
cells = [list() for row in range(side)]
for r in range(side):
    for c in range(side):
        cells[r].append(z3.Int('cell_%d_%d' % (r, c)))
