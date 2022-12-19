import os
import numpy as np
import pandas as pd
from io import StringIO

file = 'residuals.dat'
path_case = os.getcwd()
path_file = os.path.join(path_case,'postProcessing','residuals','0', file)

def get_residuals():
    with open(path_file,'r') as f:
        content = f.read()
        content = content.split('\n')
        del content[0]
        del content[1]
        contentIO = StringIO('\n'.join(content))

    data = pd.read_csv(contentIO, delimiter='\t')
    data.columns = ['Time','p','Ux','Uy','k','omega']

    return data