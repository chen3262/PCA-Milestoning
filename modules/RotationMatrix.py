import numpy as np
def RotationMatrix(Xp,Yp,X,Y,r):
    RotM = []
    vec0 = np.array([1,0])
    for i in range(len(X)):
        vec1 = np.array([Xp[i]-X[i], Yp[i]-Y[i]])
        theta = np.arccos( np.dot(vec1.T, vec0)/r )
        if vec1[1]<0:
            theta = 2*np.pi-theta

        c, s = [np.cos(theta), np.sin(theta)]
        rot = np.array([[c, s],[-s, c]]).reshape(2,2)
        RotM.append(rot)
    RotM = np.asarray(RotM)
    
    return(RotM)
