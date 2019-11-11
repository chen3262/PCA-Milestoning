import numpy as np
from log_progress import*

def area(x1,y1,x2,y2,x3,y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)

def SortByMilestones(Xp, Xn, Yp, Yn, PCA1, PCA2):
    
    x1,y1=[Xp[:-1],Yp[:-1]]
    x2,y2=[Xn[:-1],Yn[:-1]]
    x3,y3=[Xp[1:],Yp[1:]]
    A1 = area(x1,y1,x2,y2,x3,y3)
    x1,y1=[Xn[1:],Yn[1:]]
    x2,y2=[Xn[:-1],Yn[:-1]]
    x3,y3=[Xp[1:],Yp[1:]]
    A2 = area(x1,y1,x2,y2,x3,y3)
    Acell = A1+A2

    midx=np.empty(len(PCA1))
    midx.fill(2*len(Xp))
    
    for i in log_progress(range(len(Xp)-1)):
        x1,y1=[Xp[i],Yp[i]]
        x2,y2=[Xn[i],Yn[i]]
        x3,y3=[Xn[i+1],Yn[i+1]]
        x4,y4=[Xp[i+1],Yp[i+1]]
        x,y=[PCA1[:],PCA2[:]]
        a1 = area(x,y,x1,y1,x2,y2)
        a2 = area(x,y,x2,y2,x3,y3)
        a3 = area(x,y,x3,y3,x4,y4)
        a4 = area(x,y,x4,y4,x1,y1)
        A = a1+a2+a3+a4
        index = abs(A-Acell[i][0])<10**-7
        midx[index]=i
    return midx  
