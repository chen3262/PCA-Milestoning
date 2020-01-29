# PCA-Milestoning
The jupyter notebooks in this repository will teach the user how to adapt the original milestoning theory to the reaction coordinates and milestones projected in 2-dimensional principal components. We will complete the rest of the tutorial asap. Now, the following three tutorials will cover principal component analysis (PCA) of MD trajectories, generate and optimize milestones, extract representative molecular configurations of milestones, and H-bond analysis of milestones. The current release include four notebooks, which should be run in the following order.

## Components
**Milestoning_Generate.ipynb** PCA of MD trajectories, construct and optimize milestones. Example optimized milestones in 2-dimentinoal principal component spaces is shown below:

<img src ="https://github.com/chen3262/PCA-Milestoning/blob/master/cover.png" width="600">

**RepreFrames_sparse.ipynb** Generating representative frames of milestones using sparse trajectories from metadynamics

**Analysis-Hbond.ipynb** Performing protein-ligand and protein-solvent-ligand H-bond analysis at each milestone. 

**Project2PCA.py** A python script to project short MD trajectories into first two principal axes

**Milestoning_Calculations.ipynb** Use milestoning theory to compute useful theromodynmics and kinetics properties, including potential of mean force (PMF), unbinding free energy, mean first passage time (MFPT) of dissociation.

## Requirements
python modules: ```numpy```, ```pytraj```, ```matplotlib```, ```scikit-learn```, ```pandas```

To check if you have these modules installed (excepting ```pytraj```), you can either do
```bash
conda list | grep "module_name"
pip list | grep "module_name"
```
If nothing is shown, you will need to install the module using either of the following commands
```bash
conda install module_name
pip install module_name
```
```pytraj``` is by default installed with ```Amber18```. If you don't have it, do either of the following commands to install ```pytraj```
```bash
conda install -c ambermd pytraj
pip install -i https://pypi.anaconda.org/ambermd/simple pytraj
```

## To use the notebook
```ruby
cd "path of the PCA-Milestoning folder"

jupyter notebook
```

## License

Copyright (C) 2019 Si-Han Chen chen.3262@osu.edu
