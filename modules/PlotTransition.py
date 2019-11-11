import matplotlib.pyplot as plt
import numpy as np

def PlotTransition(TRANS, PCA1, PCA2, Xn, Xp, Yn, Yp, T, sc=20, trans_id=0, hit_type=0):
    N, ini, fin = TRANS[TRANS[:,-1]==hit_type][trans_id,[0,3,4]] # traj id, initial id, final id
#     print("Transition type:\t%s"%hit_type)
    print("Short MD ID:\t%s"%N)
    print("Initial frame:\t%s"%ini)
    print("Final frame:\t%s"%fin)

    trjx = PCA1[N*T:(N+1)*T]
    trjy = PCA2[N*T:(N+1)*T]

    plt.figure(figsize=(8,8))

    for i in range(len(Xn)):
        if i==0:
            plt.plot([Xn[i,0], Xp[i,0]],[Yn[i,0], Yp[i,0]],'-',
                 color='k', linewidth=1,label='milestones')
        else:
            plt.plot([Xn[i,0], Xp[i,0]],[Yn[i,0], Yp[i,0]],
                     '-',color='k', linewidth=1)

    plt.plot(trjx,trjy,color='gray', alpha=0.5, zorder=0)
    plt.scatter(trjx[ini:fin+2], trjy[ini:fin+2], 
                s=20, 
                c=range(int(fin+2-(ini))), 
                zorder=3
               )
    plt.plot(trjx[np.max([0,ini-2]):fin+2], trjy[np.max([0,ini-2]):fin+2],
             color='k', zorder=1
            )
    plt.scatter([trjx[ini],trjx[fin]], [trjy[ini],trjy[fin]],
                marker='x', s=200,
                c='r', zorder=2
               )

    plt.xlabel('PC1', fontsize=16)
    plt.ylabel('PC2',fontsize=16)
    plt.tick_params(labelsize=12)
#     plt.xlim([min(trjx)-1,max(trjx)+1])
#     plt.ylim([min(trjy)-1,max(trjy)+1])
    plt.show()