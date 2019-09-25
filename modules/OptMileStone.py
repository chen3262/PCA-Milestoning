import sys
sys.path.append('./modules/')
import numpy as np
from Project import*

def OptMileStone(x, y, xp, yp, xn, yn, slopeopt, step=0.05, niter=20):
    pd1, pd2 = [np.array([0.0]*len(slopeopt)*2).reshape(len(slopeopt),2) for i in range(2)]
    for j in range(niter):
        for i in range(1,len(slopeopt)):
            d1 = (xp[i] - xp[i-1])**2 + (yp[i] - yp[i-1])**2
            d2 = (xn[i] - xp[i-1])**2 + (yn[i] - yp[i-1])**2
            if d1>d2:
                tmpx, tmpy = [xp[i], yp[i]]
                xp[i], yp[i] = [xn[i], yn[i]]
                xn[i], yn[i] = [tmpx, tmpy]
        for i in range(1,len(slopeopt)-1):
            ip1 = max(i-1, 0)
            ip2 = min(i+1, len(slopeopt))
            pp11 = Project([xp[i],yp[i]], [xp[ip1],yp[ip1]], [x[ip1],y[ip1]])
            pp12 = Project([xp[i],yp[i]], [xp[ip2],yp[ip2]], [x[ip2],y[ip2]])
            pp21 = Project([xn[i],yn[i]], [xn[ip1],yn[ip1]], [x[ip1],y[ip1]])
            pp22 = Project([xn[i],yn[i]], [xn[ip2],yn[ip2]], [x[ip2],y[ip2]])
            mid1_x, mid1_y = [(pp11[j]+pp12[j])/2 for j in range(2)]
            mid2_x, mid2_y = [(pp21[j]+pp22[j])/2 for j in range(2)]
            pd1[i,0], pd1[i,1] = [(mid1_x-xp[i])*step, (mid1_y-yp[i])*step ]
            pd2[i,0], pd2[i,1] = [(mid2_x-xn[i])*step, (mid2_y-yn[i])*step ]
            
        pd1[0,0], pd1[0,1] = [pd1[1,0], pd1[1,1]]
        pd2[0,0], pd2[0,1] = [pd2[1,0], pd2[1,1]]
        xp += pd1[:,0].reshape(len(xp),1)
        yp += pd1[:,1].reshape(len(xp),1)
        xn += pd2[:,0].reshape(len(xp),1)
        yn += pd2[:,1].reshape(len(xp),1)
    
    # slope array N*1
    #global slope_opt 
    #slope_opt = (yp-y)/(xp-x)
    return (yp-y)/(xp-x)
