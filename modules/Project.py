import numpy as np
def Project(P, M, P1):
    PM_x = P[0]-M[0]
    PM_y = P[1]-M[1]
    P1M_x = P1[0]-M[0]
    P1M_y = P1[1]-M[1]
    L = P1M_x*P1M_x + P1M_y*P1M_y
    p = PM_x*P1M_x + PM_y*P1M_y
    pp_x = M[0] + p/L*P1M_x
    pp_y = M[1] + p/L*P1M_y
    return np.array([pp_x, pp_y])
