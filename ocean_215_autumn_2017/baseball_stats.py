"""

This script cleans up CSV files containing baseball statistics for Assignment 2.

Names are reformatted, ranks are deleted, entries are shuffled, data is encoded to ASCII, and new CSV file is exported.

"""


import numpy as np
import pandas as pd
import unicodedata
import re

# inputs
filename = 'AL_batters_original.csv'
filename_new = 'AL_batters.csv'
filepath = '/Users/Ethan/Documents/UW/By course/2017-09 - serving as TA for OCEAN 215 (Stephen C. Riser)' \
           '/2017-10-TBD - assignment 2/'
data = pd.read_csv(filepath + filename,delimiter=',',header=0,encoding='utf8')

# remove rank column
data = data.drop('Rk',1)

# clean up names using transcoding and regular expressions
new_names = data['Name'].values
new_names = np.array([unicodedata.normalize('NFKD',name_str) for name_str in new_names])
name_regexp = re.compile('(.*?)\*?#?\\\\.*')
new_names = np.array([name_regexp.findall(name_str)[0] for name_str in new_names])
data['Name'] = new_names

# shuffles into random order
data = data.sample(frac=1)

# exports to CSV
data.to_csv(filepath + filename_new,sep=',',float_format='%.3f',header=True,index=False,encoding='ascii')

# test loading columns with strings (dtype='str' is necessary)
names,teams = np.loadtxt(filepath + filename_new,dtype='str',delimiter=',',skiprows=1,usecols=(0,2),unpack=True)

# test loading columns with floats (dtype='float' is optional)
ages,batting_avgs = np.loadtxt(filepath + filename_new,dtype='float',delimiter=',',skiprows=1,usecols=(1,16),unpack=True)
