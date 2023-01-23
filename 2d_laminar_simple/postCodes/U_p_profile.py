import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path_current_L = os.path.dirname(os.path.realpath(__file__)).split("\\")
path_current_L.pop()
path_case = "\\".join(path_current_L)

def get_profile(X,field,case):

    path_post = os.path.join(path_case,'postProcessing','U_p_profile',str(case.endTime),f'{X}_{field}.xy')
    fields_df = pd.read_csv(path_post, sep='\t', header=None)

    if field=='U':
        fields_df.columns = ['y','Ux','Uy','Uz']
        fields_df.drop('Uy', inplace=True, axis=1)
        fields_df.drop('Uz', inplace=True, axis=1)
        fields_df['Ux'] = fields_df['Ux']*100
    elif field=='p':
        fields_df.columns = ['y','p']

    fields_df['y'] = fields_df['y']*1000

    return fields_df


if __name__=='__main__':
    pass

