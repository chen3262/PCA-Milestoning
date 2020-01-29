import sys
sys.path.insert(1,'/hdd/si_han/cpptraj_test/pytraj')
import pytraj as pt
from sklearn.decomposition import PCA
import numpy as np
import pandas as pd

# Set file paths and parameters
TRAJ = '/hdd/si_han/Project/CDK8/metadynamics/WeiChen_VM2_candidates/002_C301-8809/100ns_seed6_restrt/nowater_combined.dcd' # a metadynamics trajectory (protein + ligand only)
TOP = '/hdd/si_han/Project/CDK8/MD/WeiChen_VM2_candidates/002_C301-8809/00.prep/06_tleap/GB.prmtop' # parameters of the trajectory
PDB = '/hdd/si_han/GPU0/sh_tzy/CDK8/milestoning/metadynamics/CDK8_Cyclin_Ligand2/new/0.pdb' # a reference protein confformation to align the trajectory
mask = '(:1-359)&(@N,@C,@CA,@O)' # atoms used for alignment, change this according to your system
pca_sel_rule = ['@CA,:620', '!@H*'] # atoms used in PCA
DIR='/hdd/si_han/ShortMD_tmp/WeiChen_VM2_candidates/002_C301-8809'
it=501 # First index of the short MD simulation folder (e.g. it=0 for P0)
en=1027 # Last index of the short MD simulation folder (e.g. it=6000 for P6000)
frq=1 # frequencing of the folder index, e.g. frq=10 if your folders are P0, P10, ... P5990, P6000
iit=1 # first replica in the above P* folder
ien=10 # last replica  in the above P* folder

#################################################################################################
######### Don Not Change Anything After This Line Unless You Know What You Are Doing ############
#################################################################################################

# Step 1: load metadynamics trajectory (to perform PCA)
traj = pt.load(TRAJ, TOP)

# Step 2: superpose the protein to a reference structure, provided as refpdb
refpdb = pt.iterload(PDB )
pt.superpose(traj, ref=refpdb, mask=mask)


# Step 3: read the metadynamics trajectory into memory by chunk
print("Loading metadynamics trajectories")
nframe = traj.n_frames
chunksize = min([200, nframe])
nchunk = int(np.floor(nframe/chunksize))+1 if nframe%chunksize !=0 else int(np.floor(nframe/chunksize))
pile = []
for i in range(nchunk):
    tmp = traj[i*chunksize:min((i+1)*chunksize, nframe)][pca_sel_rule[0]][pca_sel_rule[1]]
    pile.append(tmp.xyz.reshape(tmp.n_frames, tmp.n_atoms*3))


# Step 3: Standardize data (Cartesian coordinates of selected atoms) for PCA
proteinUNK_2d = np.concatenate(pile,axis=0)[:4700]
refframe =  proteinUNK_2d[0,:]
proteinUNK_ref_2d = proteinUNK_2d - refframe
proteinUNK_2d = proteinUNK_2d - proteinUNK_2d.mean(axis=0)

# Step 4: PerformPCA using sklearn
print("Calculating principal components")
pca = PCA(n_components=2)
reduced_cartesian = pca.fit_transform(proteinUNK_2d)
print(reduced_cartesian.shape)

# obtain eigvals and eigvecs
eigvals = pca.explained_variance_ratio_
eigvecs = pca.components_.T


# Step 5: Prroject short MD simulations to PC1/PC2 space
print("Projecting short MD simulations to PC1/PC2 space")

index =[]
pca1 = []
pca2 = []

while it <= en:
    print("On Configuration "+str(it))
    nit=iit
    nen=ien
    while nit <= nen:
        mdtraj = pt.iterload(DIR+'/P'+str(it)+'/02.MD'+str(nit)+'/MD1_unwrap.dcd', 
                             TOP)
        print("\tReplica "+str(nit)+" "+str(len(mdtraj))+" frames\r")

        pt.superpose(mdtraj, ref=refpdb, mask=mask)
        
        mdtmp = mdtraj[pca_sel_rule[0]][pca_sel_rule[1]]
        
        # shift to the reference frame
        mdtmp2 = mdtmp.xyz.reshape(mdtmp.n_frames, mdtmp.n_atoms*3)-refframe

        pca1.append(np.dot(mdtmp2, eigvecs[:,0]))
        pca2.append(np.dot(mdtmp2, eigvecs[:,1]))
        index.append([it]*mdtmp.n_frames)
        nit = nit+1
    it = it+frq

########### I/O projections to a file #########
print("writing outputs to "+DIR)
PCA1 = np.concatenate(pca1,axis=0)
PCA2 = np.concatenate(pca2,axis=0)
IDX = np.concatenate(index,axis=0)

np.save(DIR+'/PCA1a.npy',PCA1)
np.save(DIR+'/PCA2a.npy',PCA2)
np.save(DIR+'/IDXa.npy',IDX)

print("Done")
