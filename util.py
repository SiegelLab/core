from db.amino_acid import THREE_to_one 

def diff_pdb( native, design ):
  '''Takes two PDB files open as files and returns a string \
     representation of the sequence differences between them'''

  wt_table = { l.split()[5]: l.split()[3] for l in native if l.startswith('ATOM') } 
  des_table = { l.split()[5]: l.split()[3] for l in design if l.startswith('ATOM') } 
  l = [] 

  for key, value in des_table.items():
    if wt_table[ key ] == value:
      pass
    else:
      l += [ '%s%s%s' % ( THREE_to_one( wt_table[ key ] ) , key, THREE_to_one( value ) ) ]

  return '+'.join( l ) 

