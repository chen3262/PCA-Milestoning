import numpy as np
def findnorm(fp):
    slope = np.array([[None]*len(fp)],dtype=float).reshape(len(fp),1)
    for i in range(len(fp)-1):
        slope[i] = -(fp[i+1,0] - fp[i,0])/(fp[i+1,1] - fp[i,1])
    slope[-1]=slope[-2]
    return slope
