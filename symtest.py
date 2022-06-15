from sympy import *
w = Symbol("w")
L1 = Symbol("L1")
C1 = Symbol("C1")
L2 = Symbol("L2")
C2 = Symbol("C2")
R2 = Symbol("R2")
Req = Symbol("Req")
M12 = Symbol("M12")
exp = (w*L1-1/(w*C1))-(w*w*M12*M12*(w*L2-1/(w*C2)))/((R2+Req)*(R2+Req)+(w*L2-1/(w*C2))*(w*L2-1/(w*C2)))
lists = solve(exp,w)
print(lists)

