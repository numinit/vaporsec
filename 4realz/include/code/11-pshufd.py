# Create the permuted flag, add trivially true constraints
shuf = [z3.BitVec('pshufd_%d' % i, 8) for i in range(16)]

smt.add(
    z3.And(shuf[0] == flag[8], shuf[1] == flag[9],
           shuf[2] == flag[10], shuf[3] == flag[11], ...)
)
