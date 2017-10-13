if smt.check() == z3.unsat:
    print('Formula was unsatisfiable :-(')
else:
    print('Formula was satisfiable.')
    model = smt.model()
    flag_str = 'flag'
    for i in range(16):
        flag_str += chr(model[flag[i]].as_long())

    print(flag_str)
