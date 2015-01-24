def rc(seq):
  c = [{'a':'t', 't':'a', 'g':'c', 'c':'g', 'A':'T', 'C':'G', 'T':'A', 'G':'C', }[i] for i in str(seq)] 
  return ''.join(c)[::-1]

aa = { 'ata':'i', 'atc':'i', 'att':'i', 'atg':'m', 'aca':'t', 'acc':'t', 'acg':'t', 'act':'t', 'aac':'n', 'aat':'n', 'aaa':'k', 'aag':'k', 'agc':'s', 'agt':'s', 'aga':'r', 'agg':'r', 'cta':'l', 'ctc':'l', 'ctg':'l', 'ctt':'l', 'cca':'p', 'ccc':'p', 'ccg':'p', 'cct':'p', 'cac':'h', 'cat':'h', 'caa':'q', 'cag':'q', 'cga':'r', 'cgc':'r', 'cgg':'r', 'cgt':'r', 'gta':'v', 'gtc':'v', 'gtg':'v', 'gtt':'v', 'gca':'a', 'gcc':'a', 'gcg':'a', 'gct':'a', 'gac':'d', 'gat':'d', 'gaa':'e', 'gag':'e', 'gga':'g', 'ggc':'g', 'ggg':'g', 'ggt':'g', 'tca':'s', 'tcc':'s', 'tcg':'s', 'tct':'s', 'ttc':'f', 'ttt':'f', 'tta':'l', 'ttg':'l', 'tac':'y', 'tat':'y', 'taa':'_', 'tag':'_', 'tgc':'c', 'tgt':'c', 'tga':'_', 'tgg':'w'} 
cod = { 'g':'ggc', 'a':'gcg', 'v':'gtg', 'f':'ttt', 'e':'gaa', 'd':'gat', 'n':'aac', 'h':'cat', 'p':'ccg', 'q':'cag', 'w':'tgg', 'y':'tat', 'i':'att', 'm':'atg', 'c':'tgc', 'k':'aaa', 'l':'ctg', 'r':'cgt', 't':'acc', 's':'agc'}

def one(three): return {'ala': 'a', 'arg': 'r', 'asn': 'n', 'asp': 'd', 'cys': 'c', 'glu': 'e', 'gln': 'q', 'gly': 'g', 'his': 'h', 'ile': 'i', 'leu': 'l', 'lys': 'k', 'met': 'm', 'phe': 'f', 'pro': 'p', 'ser': 's', 'thr': 't', 'trp': 'w', 'tyr': 'y', 'val': 'v', 'unk': 'x'}[three.group(0)]

aa1_upper = list("ACDEFGHIKLMNPQRSTVWY")
aa1_lower = list("acdefghiklmnpqrstvwy")
aa3_upper = "ALA CYS ASP GLU PHE GLY HIS ILE LYS LEU MET ASN PRO GLN ARG SER THR VAL TRP TYR".split()
aa3_lower = "ala cys asp glu phe gly his ile lys leu met asn pro gln arg ser thr val trp tyr".split()

def one_to_three(residue_as_1_letter_code):
  return dict( zip(aa1_lower, aa3_lower) )[residue_as_1_letter_code]

def one_to_THREE(residue_as_1_letter_code):
  return dict( zip(aa1_lower, aa3_upper) )[residue_as_1_letter_code]
  
def ONE_to_three(residue_as_1_letter_code):
  return dict( zip(aa1_upper, aa3_lower) )[residue_as_1_letter_code]

def ONE_to_THREE(residue_as_1_letter_code):
  return dict( zip(aa1_upper, aa3_upper) )[residue_as_1_letter_code]

def three_to_one(aa):
  return dict(zip(aa3_lower, aa1_lower))[aa]

def three_to_ONE(aa):
  return dict(zip(aa3_lower, aa1_upper))[aa]

def THREE_to_one(aa):
  return dict(zip(aa3_upper, aa1_lower))[aa]

def THREE_to_ONE(aa):
  return dict(zip(aa3_upper, aa1_upper))[aa]
