__author__ = 'stevebertolani'

from os import chdir
from pdb_structure import *
from sys import argv
from pandas import DataFrame
from pandas import read_csv
from os import curdir
from scorefile_reader.Score import ScoreFile
from Contact.Contact import ContactCounter

df_contacts = DataFrame()
fh = open(argv[1],'r')
mybasepath = curdir


for name in fh:


    print(name)
    #change into directory that has the score.sc file

    name_path = mybasepath+"/"+name
    chdir(name_path)
    #read the score.sc and get the lowest energy based on the input tag
    data = read_csv("score.sc",delim_whitespace=True,header=0) # Note, the header may not be the first line
    sf2 = ScoreFile(data)
    lowest_pdb = sf2.return_lowest_energy_tag(tag="score")
    print("The lowest energy pdb file is %s" %lowest_pdb)

    cutoff = 8
    activestruct = activesitestructure_from_file( lowest_pdb , cutoff, name)
    ctct = ContactCounter( activestruct )
    print(ctct.print_contact_results())
    #df_contacts.append( ctct.series )
    #print df_contacts

#df_contacts.write_csv("ContactCounterResults")