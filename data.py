import pickle as pickle
import pandas as pd 
df=pd.read_pickle('playerdata')
compression_opts = dict(method='zip',archive_name='out.csv')  

df.to_csv('out.zip', index=False,compression=compression_opts)  


