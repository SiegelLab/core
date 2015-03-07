from core.db.amino_acid import cod, one, rc, aa_from_codon
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-p', help='plain text output (default is JSON)')
parser.add_argument('fasta', help='nucleotide FASTA')
parser.add_argument('list', help='text file containing a list of mutants to make') 
parser.add_argument('scaffold', help='scaffold name') 
args = parser.parse_args()

with open(args.fasta, 'r') as f:
  gene = f.readlines()
  gene = gene[1:] if re.match(r'>', gene[0]) else gene
  gene = re.sub( r'[\n \d+]', '', ''.join(gene).lower() )

with open(args.list, 'r') as l:
  lis = l.read().lower()
  if not lis[1].isdigit():
    lis = re.sub(r'[A-Za-z]{3}', one, lis).split()
  else: 
    lis = lis.split()

for line in lis:
  seq = [gene[i:i+3] for i in range(0, len(gene), 3)]
  l = []
  switches = re.split(r'\+', line)
  for switch in switches:
    old, *i, new = switch
    i = int(''.join(i))
    ori = aa_from_codon( seq[i-1] )
    assert old is ori, 'error: you say ' + old + ' but seq has ' + ori
    seq[i-1] = cod[new].upper()
    l += [i]

  if l:
    e = rc(''.join(seq[min(l)-6:max(l)+4]))
    e = re.sub(r'([atcg]{15})[atcg]{0,}([atcg]{15})', r'\1,\2', e)
    list_of_oligos = e.split(r',') 

  mutant_handle = '+'.join(switches)
  j = { 'handle': mutant_handle, 'oligos': list_of_oligos, 'ssDNA': str( args.scaffold ) } 
  print ( j ) 

