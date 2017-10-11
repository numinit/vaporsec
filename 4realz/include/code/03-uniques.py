# Rows must have unique values
for r in range(side):
    this_row = [cells[r][c] for c in range(side)]
    smt.add(z3.Distinct(*this_row))

# Columns must have unique values
for c in range(side):
    this_col = [cells[r][c] for r in range(side)]
    smt.add(z3.Distinct(*this_col))
