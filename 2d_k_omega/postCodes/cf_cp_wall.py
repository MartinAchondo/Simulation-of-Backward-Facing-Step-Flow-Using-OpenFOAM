import os
import numpy as np
import pandas as pd

endTime = 100

path_case = os.getcwd()
path_post = os.path.join(path_case,'postProcessing','cf_cp_surface',str(endTime))

def get_cf():
    cf_lower_1 = pd.read_csv(os.path.join(path_post,'lower_1_cf.xy'), sep='\t', header=None)
    cf_lower_1.columns = ['x','cf','cfy','cfz']
    cf_lower_2 = pd.read_csv(os.path.join(path_post,'lower_2_cf.xy'), sep='\t', header=None)
    cf_lower_2.columns = ['x','cf','cfy','cfz']
    cf_lower = pd.concat([cf_lower_1,cf_lower_2], ignore_index=True)

    cf_upper = pd.read_csv(os.path.join(path_post,'upper_cf.xy'), sep='\t', header=None)
    cf_upper.columns = ['x','cf','cfy','cfz']

    return cf_lower,cf_upper
    

def get_cp():
    cp_lower_1 = pd.read_csv(os.path.join(path_post,'lower_1_cp.xy'), sep='\t', header=None)
    cp_lower_1.columns = ['x','cp']
    cp_lower_2 = pd.read_csv(os.path.join(path_post,'lower_2_cp.xy'), sep='\t', header=None)
    cp_lower_2.columns = ['x','cp']
    cp_lower = pd.concat([cp_lower_1,cp_lower_2], ignore_index=True)

    cp_upper = pd.read_csv(os.path.join(path_post,'upper_cp.xy'), sep='\t', header=None)
    cp_upper.columns = ['x','cp']

    return cp_lower,cp_upper
