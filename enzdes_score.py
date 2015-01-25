import pandas 

def lowest_by_percent(df, percent=0.1, col='total_score'):
  '''Returns the lowest 10% by total_score by default'''
  return df[(df[col] < df[col].quantile(percent))]

def lowest_by_std_dev(df, std_dev=1, col='total_score'):
  '''By default, provides the structures with a score less than 1 standard deviation
     from the median total_score'''
  return df[ ( df[col] < df[col].median() - ( std_dev * df[col].std(axis=1) ) ) ]

def constraint_cutoff(df, cutoff=10, col='all_cst'):
  return df[(df[col] < cutoff)] 
    
def read_scorefile(path):
  return pandas.read_csv(path, delimiter=r'\s+')
