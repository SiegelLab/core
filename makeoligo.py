from core.db.amino_acid import * 
from sys import argv
import re

if len(argv) < 3: 
  print("usage: python3 makeoligo.py <fasta> <list>")
  exit()

# io
# get nucleotide sequence as a string
with open(argv[1], 'r') as f:
  gene = f.readlines()
  gene = gene[1:] if re.match(r'>', gene[0]) else gene
  gene = re.sub( r'[\n \d+]', '', ''.join(gene).lower() )
  # make this for gene in genes :P

# get a list of mutations to make 
with open(argv[2], 'r') as l:
  lis = l.read().lower()
  if not lis[1].isdigit():
    lis = re.sub(r'[a-z]{3}', three_to_one, lis).split()
  else: 
    lis = lis.split()

# procedure 
for line in lis:
  seq = [gene[i:i+3] for i in range(0, len(gene), 3)]
  l = []
  switches = re.split(r'\+', line)
  for switch in switches:
    old, *i, new = switch
    i = int(''.join(i))
    ori = aa_from_codon( seq[i-1] )
    if old is ori:
      seq[i-1] = cod[new].upper()
      l += [i]
    else :
      e = 'error: you say ' + old + ' but seq has ' + ori
      break
  if l:
    e = rc(''.join(seq[min(l)-6:max(l)+4]))
    e = re.sub(r'([atcg]{15})[atcg]{0,}([atcg]{15})', r'\1,\2', e)
  print('+'.join(switches) + ',' + e)
