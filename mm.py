import pandas
from scipy.optimize import curve_fit
from scipy.stats import linregress
from numpy import linspace
import matplotlib.pyplot as plt
import argparse 

parser = argparse.ArgumentParser()
parser.add_argument('csv', help='CSV data file with required columns "sample", \
  "yield", "kobs", and "s" (substrate concentraton)')
args = parser.parse_args()

def mm(S, kcat, km): return kcat*S/(km+S)
def si(S, kcat, km, ki): return kcat*S/(km+S*(1+S/ki))
def f(m, x, b): return m*x+b

def fit(data):
  # linear params
  slope, intercept, r_value, p_value, std_err = linregress(data['s'], data['kobs'])
  
  # michaelis menten params
  p0 = ( data['kobs'].max(), data['s'].mean() )
  (kcat, km), cov = curve_fit(mm, data['s'], data['kobs'], p0=p0) 
  err1, err2 = [ abs(cov[i][i])**0.5 for i in range(2) ]
  
  # substrate inhibition params
  try:
    p0 = ( data['kobs'].max(), data['s'].mean(), data['s'].mean() )
    (si_kcat, si_km, ki), si_cov = curve_fit(si, data['s'], data['kobs'], p0=p0)
    err4, err5, err6 = [ abs(si_cov[i][i])**0.5 for i in range(3) ]
  except:
    si_kcat, si_km, ki, err4, err5, err6 = [ False ] * 6

  # splines for the various fits
  mm_x = lm_x = si_x = linspace(0,max(data['s']))
  mm_y = [mm(xx,kcat,km) for xx in mm_x]
  si_y = [si(xx,si_kcat,si_km,ki) for xx in si_x]
  lm_y = [f(slope,xx,intercept) for xx in lm_x]
  
  result = { 
    'yield': data['yield'].iget(0),
    'x': data['s'],
    'y': data['kobs'],

    'kcat': kcat, 
    'err1': err1, 
    'km': km, 
    'err2': err2, 

    'slope': slope,
    'std_err': std_err, 
    'R': r_value,

    'si_kcat': si_kcat,
    'si_km': si_km,
    'ki':  ki,
    'err_si_kcat': err4,
    'err_si_km': err5,
    'err_ki': err6,

    'mm_x': mm_x, 
    'mm_y': mm_y,
    'lm_x': lm_x, 
    'lm_y': lm_y,
    'si_x': si_x, 
    'si_y': si_y,
  }
  return pandas.Series(result)

# io
plates = pandas.read_csv(args.csv)
fits = plates.groupby(by='sample').apply(fit)
fits.to_csv('raw-out.csv', columns=('yield', 'kcat', 'err1', 
  'km', 'err2', 'slope', 'std_err', 'R', 'ki', 'err6', )) 

# plots
for sample, fit in fits.iterrows():
  print('Plotting sample %s' % sample)

  fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(18,5))
  fig.suptitle('Sample %s with yield %1.2f mg/mL' % (sample, fit['yield'], ),
    fontsize=16)
  fig.subplots_adjust(bottom=0.1, top=0.70) # make room for labels

  axes[0].scatter(fit['x'], fit['y'])
  axes[0].plot(fit['lm_x'], fit['lm_y'])
  axes[0].set_title('Linear\nslope = %.0d\nr = %.2f' % (fit['slope'], fit['R'], ))
  axes[0].set_ylabel('Rate observed (1/min)')

  axes[1].scatter(fit['x'], fit['y'])
  axes[1].plot(fit['mm_x'], fit['mm_y'])
  axes[1].set_title("Michaelis-Menten\nkcat=%2.0f ± %0.2f%%\nkm = %1.4f ± %0.2f%%" % (fit['kcat'],
    fit['err1']/fit['kcat']*100, fit['km'], fit['err2']/fit['km']*100))
  axes[1].set_xlabel('4-nitrophenyl-ß-D-glucoside (M)') 
  
  axes[2].scatter(fit['x'], fit['y'])
  axes[2].plot(fit['si_x'], fit['si_y'])
  if fit['ki'] == False:
    axes[2].set_title("No substrate inhibition fit") 
  else:
    axes[2].set_title("Michaelis-Menten with substrate inhibition\
      \nkcat = %.0f ± %2.0f%%\nkm = %1.4f ± %2.0f%%\nki = %1.4f ± %2.0f%%" % (fit['kcat'],
      fit['err1']/fit['kcat']*100, 
      fit['km'], 
      fit['err2']/fit['km']*100,
      fit['ki'], fit['err6']/fit['ki']*100),)

  fig.savefig('plots/%s.svg' % sample)
  plt.close()
