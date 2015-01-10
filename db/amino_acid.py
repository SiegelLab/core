def rc(seq):
  c = [{'a':'t', 't':'a', 'g':'c', 'c':'g', 'A':'T', 'C':'G', 'T':'A', 'G':'C', }[i] for i in str(seq)] 
  return ''.join(c)[::-1]

aa = { 'ata':'i', 'atc':'i', 'att':'i', 'atg':'m', 'aca':'t', 'acc':'t', 'acg':'t', 'act':'t', 'aac':'n', 'aat':'n', 'aaa':'k', 'aag':'k', 'agc':'s', 'agt':'s', 'aga':'r', 'agg':'r', 'cta':'l', 'ctc':'l', 'ctg':'l', 'ctt':'l', 'cca':'p', 'ccc':'p', 'ccg':'p', 'cct':'p', 'cac':'h', 'cat':'h', 'caa':'q', 'cag':'q', 'cga':'r', 'cgc':'r', 'cgg':'r', 'cgt':'r', 'gta':'v', 'gtc':'v', 'gtg':'v', 'gtt':'v', 'gca':'a', 'gcc':'a', 'gcg':'a', 'gct':'a', 'gac':'d', 'gat':'d', 'gaa':'e', 'gag':'e', 'gga':'g', 'ggc':'g', 'ggg':'g', 'ggt':'g', 'tca':'s', 'tcc':'s', 'tcg':'s', 'tct':'s', 'ttc':'f', 'ttt':'f', 'tta':'l', 'ttg':'l', 'tac':'y', 'tat':'y', 'taa':'_', 'tag':'_', 'tgc':'c', 'tgt':'c', 'tga':'_', 'tgg':'w'} 
cod = { 'g':'ggc', 'a':'gcg', 'v':'gtg', 'f':'ttt', 'e':'gaa', 'd':'gat', 'n':'aac', 'h':'cat', 'p':'ccg', 'q':'cag', 'w':'tgg', 'y':'tat', 'i':'att', 'm':'atg', 'c':'tgc', 'k':'aaa', 'l':'ctg', 'r':'cgt', 't':'acc', 's':'agc'}

def one(three): return {'ala': 'a', 'arg': 'r', 'asn': 'n', 'asp': 'd', 'cys': 'c', 'glu': 'e', 'gln': 'q', 'gly': 'g', 'his': 'h', 'ile': 'i', 'leu': 'l', 'lys': 'k', 'met': 'm', 'phe': 'f', 'pro': 'p', 'ser': 's', 'thr': 't', 'trp': 'w', 'tyr': 'y', 'val': 'v', 'unk': 'x'}[three.group(0)]
