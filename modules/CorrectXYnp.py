def CorrectXYnp(Xp,Yp,Xn,Yn, slope_opt):
    for i in range(1,len(slope_opt)):
        d1 = (Xp[i] - Xp[i-1])**2 + (Yp[i] - Yp[i-1])**2
        d2 = (Xn[i] - Xp[i-1])**2 + (Yn[i] - Yp[i-1])**2
        d3 = (Xn[i] - Xn[i-1])**2 + (Yn[i] - Yn[i-1])**2
        d4 = (Xp[i] - Xn[i-1])**2 + (Yp[i] - Yn[i-1])**2
#         if d1>d2:
        if max(d2,d4) < max(d1,d3):
            tmpx, tmpy = [Xp[i].copy(), Yp[i].copy()]
            tmpx1, tmpy1 = [Xn[i].copy(), Yn[i].copy()]
            Xp[i], Yp[i], Xn[i], Yn[i] = [tmpx1, tmpy1, tmpx, tmpy]
