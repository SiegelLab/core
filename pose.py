from re import match
#from db.atom import radii 

class Atom:
  def __init__(self, l):
    '''Create atom from line in PDB'''

    self.record = l[0:6].strip()
    self.number = int(l[6:11])
    self.atomname = l[12:16].strip()
    self.altloc = l[16]
    self.aa = l[17:20]
    self.chain = l[21]
    self.seq = int(l[22:26])
    self.achar = l[26]
    self.xyz = (float(l[30:38]), float(l[38:46]), float(l[46:54]))
    self.occupancy = float(l[54:60])
    self.bfactor = float(l[60:66])
    self.seg_id = l[72:76].strip()
    self.element = l[76:78].strip()
    self.charge = float(l[79:81]) if l[70:91] == True else 0

  # instance variables  
  self.bb = 'Oh yeah' if self.atomname in ['N', 'CA', 'C', 'O'] else 'Nope'
    
    # energy 
    #self.radius = radii[self.element]

  def __repr__(self):
    '''Writes valid PDB according to specification'''

    return '%-6s' % self.record + \
      '%5d ' % self.number + \
      '%-4s' % self.atomname + \
      '%1s' % self.altloc + \
      '%3s ' % self.aa + \
      '%1s' % self.chain + \
      '%4d' % self.seq + \
      '%1s   ' % self.achar + \
      '%8.3f%8.3f%8.3f' % self.xyz + \
      '%6.2f' % self.occupancy + \
      '%6.2f      ' % self.bfactor + \
      '%-4s' % self.seg_id + \
      '%-4s' % self.element + \
      '%2s' % self.charge
  
  # Measurement and other nondestructive methods  
  def dist(self, other):
    '''Cartesian distance'''
    x1, y1, z1 = self.xyz
    x2, y2, z2 = other.xyz
    return ((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)**0.5

  # Movers and other destructive methods
  def zero(self):
    '''Moves this atom to origin'''
    self.xyz = (0, 0, 0)
    
  def push(self, push):
    self.xyz = tuple(map(sum, zip(self.xyz, push)))

class PDB:
  'Represents a single PDB, use like 1sny = PDB("1sny.pdb")'
  def __init__(self, fn): 
    fn = open(fn).readlines()
    
    self.remark = [ l for l in fn if match(r'^REMA', l) ]
    self.atom = [ Atom(l) for l in fn if match(r'^ATOM', l) ]
    self.hetatm = [ Atom(l) for l in fn if match(r'^HETA', l) ] 
    self.allatm = self.atom + self.hetatm

    # maybe have a bunch of ways to subset?
    self.c_alpha = [ Atom(l) for l in fn if match(r'^ATO.+CA', l) ]

    self.contact_map = [ [ 1 if c.dist(i) < 10 \
      else 0 for c in self.c_alpha ] for i in self.c_alpha ]

  def __repr__(self):
    return '%s' % '\n'.join([ str(a) for a in self.remark + self.allatm ])
