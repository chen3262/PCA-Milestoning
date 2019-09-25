# PCA-Milestoning
Clustering protein conformations using different RMSD inputs:

```Clustering-K-Means-RMSD-CA.ipynb``` clusters conformations using RMSD of Cartesian coordinates of alpha-C atoms

```Clustering-K-Means-RMSD-Rihedrals.ipynb``` clusters conformations using RMSD of phi and sin angles

```Clustering-K-Means-RMSD-mix.ipynb``` clusters conformations using both the above RMSD terms, with the RMSD of phi and sin angles multiplied by 200. A sample clustering result is shown below:

<img src ="https://github.com/chen3262/Clustering-K-Means/blob/master/K-means.png" width="600">

## Requirements
python modules: ```numpy```, ```pytraj```, ```matplotlib```, ```scikit-learn```

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
To install ```pytraj```, please do either of the following commands
```bash
conda install -c ambermd pytraj
pip install -i https://pypi.anaconda.org/ambermd/simple pytraj
```

## To use the notebook
```ruby
cd "path to Clustering-K-Means folder"

jupyter notebook
```

## License

Copyright (C) 2019 Si-Han Chen chen.3262@osu.edu
