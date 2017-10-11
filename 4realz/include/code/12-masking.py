# Masks for each round:
# ffffffff ffffff00 ffffffff ffffff00
# ffffffff ffff00ff ffffffff ffff00ff
# ffffffff ff00ffff ffffffff ff00ffff
# ffffffff 00ffffff ffffffff 00ffffff
# ... etc.
mask = [0x00 if i == round else 0xff for i in range(8)] * 2
masked = [
    z3.BitVec('m_%d_%d' % (round, i), 8) for i in range(16)
]
for i in range(16):
    smt.add(masked[i] == (shuf[i] & mask[i]))
