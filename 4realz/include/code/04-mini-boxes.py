# Each mini-box must have unique values
for r in range(0, side, order):
    for c in range(0, side, order):
        selected = []
        for i in range(box_size):
            for j in range(box_size):
                selected.append(cells[r + i][c + j])

        smt.add(z3.Distinct(*selected))
