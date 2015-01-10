import argparse 
parser = argparse.ArgumentParser()
parser.add_argument("scorefile")
args = parser.parse_args()

import pandas 
sf = pandas.read_csv(args.scorefile, delimiter=r'\s+')
sf.describe()

