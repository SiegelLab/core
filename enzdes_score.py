import pandas 

def lowest_by_percent(df, percent=0.1, col='total_score'):
  return df[(df[col] < df[col].quantile(percent))]

def lowest_by_std_dev(df, std_dev=1, col='total_score'):
  return df[(df[col] < std_dev * df[col].std)]
    
def read_scorefile(path):
  return pandas.read_csv(path, delimiter=r'\s+')


