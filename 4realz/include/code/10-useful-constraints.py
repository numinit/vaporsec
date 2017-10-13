import z3
smt = z3.Solver()
flag = [z3.BitVec('flag_%d' % i, 8) for i in range(16)]

# Flag must start with '{' and end with '}', and the rest must be ASCII
smt.add(z3.And(flag[0] == ord('{'), flag[-1] == ord('}')))
for i in range(1, 15):
    smt.add(z3.And(flag[i] >= 32, flag[i] < 127))
