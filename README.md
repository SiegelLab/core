# Scripts in this repo

## Rosetta 

### `default.enzdes.flags`

By Justin Siegel 

A default flags file for use with RosettaScripts. 

### `submit.bash` 

High-powered submission script for use on Epiphany. 


## Scripts for working with PDB files 

### `pdb_parser.py`

By Andrew Leaver-Fay, Morgan Nance, and Steve Bertolani 

A full-featured PDB parser. 


## For working with scorefiles 

### `scores.py`

By Morgan Nance and Steve Bertolani

```python
# example usage 
from score import ScoreFile
from pandas import read_csv

data = read_csv("score.sc",delim_whitespace=True,header=0) # Note, the header may not be the first line
     
sf = ScoreFile(data)
lowest_pdb = sf.return_lowest_energy_tag(tag="score") # You can put in any valid scorefile tag from the header
     
print "The lowest energy pdb file is %s" %lowest_pdb
```


### `enzdes_score.py`

By Alex Carlin

A module for reading and filtering EnzDes-style scorefiles. 

```python
# example use
from core import enzdes_score

sf = enzdes_score.read_scorefile('tests/enzdes.sc')
lowest10 = lowest_by_percent(sf, percent=0.33) 
```


### `pose.py`

By Alex Carlin

A minimal PDB parser. Usage

```python
from core import pose
mypdb = pose.from_pdb('tests/1sny.pdb')
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
