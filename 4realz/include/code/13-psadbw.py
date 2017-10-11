psadbw_lo = z3.BitVec('psadbw_lo', 16)
psadbw_hi = z3.BitVec('psadbw_hi', 16)

# Assume we have a helper that can do absolute values...
smt.add(psadbw_lo == (
    Abs(iv[0] - masked[0]) + Abs(iv[1] - masked[1]) +
    Abs(iv[2] - masked[2]) + Abs(iv[3] - masked[3]) + ...
)) # and repeat for psadbw_hi

res = [z3.BitVec('ps_%d' % i, 8) for i in range(16)]
smt.add(res[0] == psadbw_lo & 0xff)
smt.add(res[1] == (psadbw_lo >> 8) & 0xff)
smt.add(res[2] == 0) # ... etc. Read Intel docs if you care.
