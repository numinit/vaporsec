for r in range(side):
    for c in range(side):
        # Each cell must be between 0 and 15.
        # Also, this is our first constraint!
        # Add it to the solver with `smt.add`.
        smt.add(z3.And(cells[r][c] >= 0, cells[r][c] < side))
