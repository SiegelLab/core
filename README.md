## Get started on Mac OS X

Install [Homebrew](). 

Install Python3* with 

```bash 
brew install python3 
```
*Note: An alternative way would be to install Anaconda's package of python which installs "most" requirements

**Note: Although some people (Alex) prefer python3, others (Steve & Morgan) understand work in Python2 given it's widespread use. Therefore, modules written by these respective authors will most likely only work for his/her preferred version. Cheers!

This will brew a Python install and symlink it into `/usr/local/bin/`. If
you don't already `/usr/local/bin/` in your PATH, add it now. 

If you don't know what your PATH is or how to change it, it may be difficult
to follow the rest of this guide. Consult Matt Might's blog for getting
started with Unix. 

To install the required Python packages, use 

```bash
pip3 install numpy scipy pandas 
pip install numpy scipy pandas
```

*Note* you really must install for both Python 2 and Python 3. 

Clone Rosetta [rosetta_clone_tools] into `~/Applications`. It is 
recommended that you install into `~/Applications` (your user
Applications folder) rather than `/Applications` (the system 
Applications folder). 

Good things to add to your `.bashrc`:

```bash
export PATH=$PATH:/usr/local/bin:~/Applications/Rosetta/main/source/bin
export ROSETTA3_DB=~/Applications/Rosetta/main/database
```

## Rosetta 

### `default.enzdes.flags`

By Justin Siegel 

A default flags file for use with RosettaScripts. 

### `submit.bash` 

High-powered submission script for use on Epiphany. 


## Parsers 

### `pdb.py`

By Andrew Leaver-Fay, Morgan Nance, and Steve Bertolani 

A full-featured PDB parser. 

### `scores.py`

By Morgan Nance and Steve Bertolani

A EnzDes scorefile parser. 

+ Get lowest XX scoring poses

####  Example Usage:

     from scorefile_reader.Score import ScoreFile
     
     from pandas import read_csv


     data = read_csv("score.sc",delim_whitespace=True,header=0) # Note, the header may not be the first line
     
     sf2 = ScoreFile(data)
     
     lowest_pdb = sf2.return_lowest_energy_tag(tag="score")
     
     print "The lowest energy pdb file is %s" %lowest_pdb


### `pose.py`

By Alex Carlin

A minimal PDB parser. Usage

```python
from pose import PDB
mypdb = PDB('tests/1sny.pdb')
```

## Data analysis 

### `mm.py` 

By Wai Shun Mak and Alex Carlin

Fits assay data to Michaelis-Menten models. 

+ Generates statistics for linear, Michaelis-Menten, and Michaelis-Menten 
  with substrate inhibition 

+ Generates diagnostic plots 

### `bfactor.py`

Color PBDs in PyMOL, useful for looking at the effects of a lot of
mutations. 


## APIs

### HMMER API

By Steve Bertolani 

Python API for HMMER. 


## Experimental/robots/oligos/ordering

### `makeoligo.py` 

Makes oligos for Kunkel mutagenesis. 


### `kinetic_assay.py` 

Example kinetic assay for use on Transcriptic. 

+ Use with `mm.py` above to automate kinetic characterization of mutants 


## Database

### `atom_types.py`

Atom types reference 

### `amino_acid.py` 

Chemical information and translation dictionaries 

+ one-letter to three letter ('A' → 'ala') 
+ three-letter to one-letter ('ALA' → 'A') 
+ freely mix & match case 

### `ecoli_codon.py`

Reference of _E. coli_ favored codon use for making mutagenic oligos
