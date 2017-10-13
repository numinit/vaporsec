ps_lo, ps_hi = z3.BitVec('psadbw_lo', 16), z3.BitVec('psadbw_hi', 16)

smt.add(ps_lo == (
    Abs(iv[0] - masked[0]) + Abs(iv[1] - masked[1]) +
    Abs(iv[2] - masked[2]) + Abs(iv[3] - masked[3]) + ...
)) # and repeat for ps_hi. Assumes that we have an `Abs` helper.

res = [z3.BitVec('psadbw_%d' % i, 8) for i in range(16)]
smt.add(res[0] == ps_lo & 0xff)
smt.add(res[1] == (ps_lo >> 8) & 0xff)
smt.add(res[2] == 0) # ... etc. Read Intel docs if you care.
