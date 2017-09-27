# presentations

### What is it?
This is a collection of miscellaneous studies on various topics. [Jupyter](https://jupyter.org/) is required to open files with *.ipynb* extension (which are structured presentations with texts, visualizations, and code cells). However, since GitHub is able to render Jupyter notebooks, formatted outputs can be viewed via browser too.

### Where to look for details?
Each notebook from the repository contains a section with problem description. In addition, all non-trivial findings are commented near corresponding cells.

### How to run these notebooks locally?
Of course, you can modify notebooks from the repository, play with them, tune some parameters, and change experiments' settings.

To create an isolated virtual environment, install all necessary packages into it, and create Jupyter kernel with this environment, run below commands from your terminal (they work on Linux and, probably, on other operating systems).
```
cd path/to/your/destination
git clone https://github.com/Nikolay-Lysenko/presentations
cd presentations
conda create --name presentations_env --file package-list.txt python=3.6
source activate presentations_env
python -m ipykernel install --user --name=presentations_env
```

However, note that notebook named `geroproptectors_search_with_pu_learning.ipynb` is written in Python 2.7. This is done, because there are some issues with `rdkit` package for Python 3. Thus, this notebook can not be run from kernel described above. To run it, read its 'Software Requirements' section and follow instructions from there. 


