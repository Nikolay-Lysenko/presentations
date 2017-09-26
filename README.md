# presentations

### What is it?
This is a collection of miscellaneous studies on various topics. [Jupyter](https://jupyter.org/) is required to open files with *.ipynb* extension (which are structured presentations with texts, visualizations, and code cells). However, since GitHub is able to render Jupyter notebooks, formatted outputs can be viewed via browser too.

### Where to look for details?
Each notebook from the repository contains a section with problem description. In addition, all non-trivial findings are commented near corresponding cells.

### How to run these notebooks locally?
Of course, you can modify notebooks from the repository, play with them, tune some parameters, and change experiments' settings.

To do so, follow below instructions (they work on Linux and, probably, on other operating systems). First of all, run this from your terminal:
```
cd path/to/your/destination
git clone https://github.com/Nikolay-Lysenko/presentations
cd presentations
conda create --name presentations_env --file package-list.txt python=3.6
source activate presentations_env
```

If you are going to run notebooks from *geroprotectors* directory, also run this:
```
conda install -c rdkit rdkit
```
or, if above command throws a dependencies error, this:
```
conda install -c greglandrum rdkit
```

Now virtual environment is created and all required packages are installed into it. The only thing to do before notebooks can be run, is to install Jupyter kernel with the new virtual environment:
```
python -m ipykernel install --user --name=presentations_env
```

That's it.


