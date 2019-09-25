# PCA-Milestoning
The jupyter notebooks in this repository will teach the user how to adapt the original milestoning theory to the reaction coordinates and milestones projected in 2-dimensional principal components. We will complete the rest of the tutorial asap. Now, the following three tutorials will cover principal component analysis (PCA) of MD trajectories, generate and optimize milestones, extract representative molecular configurations of milestones, and H-bond analysis of milestones. In the future, we will complete this tutorial by including the calculations of potential of mean force profiles and mean first passage time of protein/ligand dissociation. 

```Milestoning_Generate.ipynb``` PCA of MD trajectories, construct and optimize milestones. Example optimized milestones in 2-dimentinoal principal component spaces is shown below:

<img src ="https://github.com/chen3262/PCA-Milestoning/blob/master/cover.png" width="600">

```RepreFrames_sparse.ipynb``` generate representative frames of milestones using sparse trajectories from metadynamics

```Analysis-Hbond.ipynb``` Perifrm protein-ligand and protein-solvent-ligand H-bond analysis at each milestone. 

## Requirements
python modules: ```numpy```, ```pytraj```, ```matplotlib```, ```scikit-learn```, ```pandas```

```pytraj``` is by default installed with ```Amber18```. To check if you have these modules installed (excepting ```pytraj```), you can either do
```bash
conda list | grep "module_name"
pip list | grep "module_name"
```
If nothing is shown, you will need to install the module using either of the following commands
```bash
conda install module_name
pip install module_name
```
To install ```pytraj```, please do either of the following commands
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
