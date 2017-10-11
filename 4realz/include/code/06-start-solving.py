if smt.check() == z3.unsat:
    print('Sudoku is impossible to solve :(')
else:
    model = smt.model()

    # Retrieve each cell from the model as a python long
    result = [list() for row in range(side)]
    for r in range(side):
        for c in range(side):
            cell = model[r][c]
            print('%x ' % model[cell].as_long(), end='')
        print()
