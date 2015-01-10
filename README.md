Siegel Lab core libraries for enzyme design with Rosetta
========================================================

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

### `pose.py`

By Alex Carlin

A minimal PDB parser. 


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
