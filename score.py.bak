__author__ = 'stevebertolani'

#import pandas as pd
from pandas import DataFrame
from pandas import read_csv
from os import path
from re import findall

file = "score.sc"

class ScoreFile(DataFrame):
    def __init__(self, *args, **kwargs):
        """
        Example Usage:

        data = read_csv(file,delim_whitespace=True,header=1)
        sf2 = ScoreFile(data)
        print sf2
        lowest_pdb = sf2.return_lowest_energy_tag(tag="total_score_no_csts")
        print "The lowest pdb in the scorefile is %s" %lowest_pdb

        """

        DataFrame.__init__(self, *args, **kwargs)
        self.check_for_cst_energies() ##automatically create new column that is constraint subtracted on instantiation of scorefile obj
        print "Created a scorefile class "

    def check_for_cst_energies(self):
        print 'Checking all the indices for the word "constraint" '
        self.list_of_score_terms = list(self.columns.values)
        self.constraint_terms_found = list()
        for i in self.list_of_score_terms:
            if (findall("constraint",i)):
                if (i.split("_")[0] != "if"):
                    self.constraint_terms_found.append(i)

        if len(self.constraint_terms_found) is 0:
            print "There are no constraint terms in this score file"
        else:
            print "Found the following terms %s " %self.constraint_terms_found
            print "Creating a new column called total_score_no_csts "

        #start the new column with the total score, then subtract off the cst column values
            try:
                self["total_score_no_csts"]=self["total_score"]
            except KeyError:
                try:
                    self["total_score_no_csts"]=self["score"]
                except:
                    print "Cannot find columns named total_score or score.... "

            for i in self.constraint_terms_found:
                self["total_score_no_csts"] -= self[i]

    def return_lowest_energy_tag(self,tag="",cst_subtraction=False):
        """
        Getting the lowest energy tag (ie, total_score or total_score_no_csts or ligand_ etc )
        """
        print "Sorting based on %s " %tag

        try:
            assert self[tag] is not None
            print "Tag %s is a valid scorefile entry, will sort on that" %tag


        except:
            print "\n !!!THAT TAG was not valid! Error %s not a valid key to dataframe" %tag

        lowest_index = self[tag].sort(["total_score_no_csts"],inplace=False).head(1)
        #print lowest_index.keys()[0]
        lowest_name = str(self.loc[[lowest_index.keys()[0]]]['description']).split()[1]
        #print lowest_name
        #print "Name for the lowest %s is %s " %(tag,lowest_name)
        return lowest_name + ".pdb"

def test():
    data = read_csv(file,delim_whitespace=True,header=0) # Note, the header may not be the first line
    sf2 = ScoreFile(data)
    print sf2
    lowest_pdb = sf2.return_lowest_energy_tag(tag="score")
    print "The lowest pdb in the scorefile is %s" %lowest_pdb

if __name__ == "__main__":
    print help( ScoreFile.__init__ )
    test()
