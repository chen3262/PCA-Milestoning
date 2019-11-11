import numpy as np
from log_progress import*

def TransitionKernel(PCA1, PCA2, MIDX, slope_mod, fp_mod, X, Y, sc, T, check_escape=True):
    
    ntraj = int(len(PCA1)/T)
    TRANS = []

    # for touching
    idx = np.array([range(len(fp_mod))]*T)
    time = np.array([[i]*len(fp_mod) for i in range(T)])
    b = Y - slope_mod*X # b of y=m*x+b

    count_crossing, count_touch = 0,0

    for N in log_progress(range(ntraj),every=1000):
        trans_tmp=[]

    ######### hit by crossing #########
        midx2 = MIDX[N*T:(N+1)*T]
        transition = midx2[1:] - midx2[:-1]
        frameid = np.array(range(len(midx2)-1))
        id1 = abs(transition) == 1

        index = id1
        frameid_trans = frameid[index]
        diff= midx2[frameid_trans+1] - midx2[frameid_trans]
        milestone = np.max(np.array([midx2[frameid_trans],midx2[frameid_trans+1]]).T, axis=1)

        if len(milestone)>0:
            m_ini,t_ini = milestone[0],frameid_trans[0]
            for i in range(len(milestone)-1):

                if (abs(milestone[i+1] - milestone[i])==1):
                    m_end, t_end = milestone[i+1], frameid_trans[i+1]
                    if m_ini != milestone[i]:
                        m_ini,t_ini = milestone[i],frameid_trans[i]

                    # check if the transition travel outside the milestone line
                    if check_escape:
                        escape = (np.any(midx2[t_ini:t_end]==2*len(fp_mod)))
                    else:
                        escape = False

                    if escape==False:
                        TRANS.append([N, m_ini, m_end, t_ini, t_end,0])
                        trans_tmp.append([N, m_ini, m_end, t_ini, t_end,0])
                        count_crossing+=1
                        m_ini, t_ini = m_end, t_end
                else:
                    continue

#     ######### hit by touching #########
#         trjx = PCA1[N*T:(N+1)*T]
#         trjx = trjx.reshape(trjx.size,1)
#         trjy = PCA2[N*T:(N+1)*T]
#         trjy = trjy.reshape(trjy.size,1)
#         midx = np.array(MIDX[N*T:(N+1)*T],dtype=int)
#         midx = np.array([midx]*len(fp_mod)).T

#         # distance between the trajectory to the milestone line
#         dist = abs(trjy + (trjx*(-slope_mod).T) - b.T)/np.sqrt(1+slope_mod**2).T
#         index1 = dist < 0.4

#         # discard trajectory out of the cutoff radius
#         index2 = midx != 2*len(fp_mod)

#         # distance between the trajectory to the path
#         dist2 = np.sqrt( (trjy-Y.T)**2 + (trjx-X.T)**2 )
#         index3 = dist2 < sc/2

#         index_hit = np.all([index1,index2,index3],axis=0)

#         idx_ = idx[index_hit]
#         time_ = time[index_hit]
#         data_ = np.concatenate((time_.reshape(time_.size,1), 
#                                 idx_.reshape(idx_.size,1)),axis=1)

#         if len(data_)>0:
#             data_ini = data_[0]
#             for i in range(len(data_)-1):

#                 if (abs(data_[i+1,1] - data_[i,1])==1):
#                     data_end = data_[i+1]
#                     if data_ini[1] != data_[i,1]:
#                         data_ini = data_[i]

#                     # check if the transition travel outside the milestone line
#                     if check_escape:
#                         escape = (np.any(midx2[data_ini[0]:data_end[0]]==2*len(fp_mod)))
#                     else:
#                         escape = False                              

#                     # exclude "hit by corssing"
#                     if len(trans_tmp) != 0:
#                         for j in range(len(trans_tmp)):
#                             if (trans_tmp[j][3]<=data_ini[0]<=trans_tmp[j][4]) or (trans_tmp[j][3]<=data_end[0]<=trans_tmp[j][4]):
#                                 break
#                             elif (data_ini[0]<=trans_tmp[j][3]<=data_end[0]):
#                                 break

#                     elif escape==False:
#                         TRANS.append([N, data_ini[1], data_end[1], data_ini[0], data_end[0],1])
#                         count_touch+=1
#                         data_ini = data_end
#                 else:
#                     continue


    TRANS = np.array(TRANS).astype(int) # (NRUN, initial milestone, final milestone, initial frame, final frame, type)
#     print('crossing: %d, touching: %d'%(count_crossing,count_touch))
    print('total transition: %s'%count_crossing)
    
    return TRANS