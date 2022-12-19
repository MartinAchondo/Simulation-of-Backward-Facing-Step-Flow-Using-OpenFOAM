import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path_current_L = os.path.dirname(os.path.realpath(__file__)).split("\\")
path_current_L.pop()
path_case = "\\".join(path_current_L)

def get_wall(X,wall,case):
    path_post = os.path.join(path_case,'postProcessing','shearStressWall',str(case.endTime),f'{X}_{wall}_wallShearStress.xy')

    tau_df = pd.read_csv(path_post, sep='\t', header=None)
    tau = abs(float(tau_df[1]))

    path_post = os.path.join(path_case,'postProcessing','wallLaw_U',str(case.endTime),f'{X}_{wall}_U.xy')
    U_df = pd.read_csv(path_post, sep='\t', header=None)
    U_df.columns = ['y','Ux','Uy','Uz']
    U_df.drop('Uy', inplace=True, axis=1)
    U_df.drop('Uz', inplace=True, axis=1)

    U_df['y'] = U_df['y']*np.sqrt(tau)/case.nu
    U_df['Ux'] = U_df['Ux']/np.sqrt(tau)

    path_post = os.path.join(path_case,'postProcessing','wallLaw_U',str(case.endTime),f'{X}_{wall}_nut.xy')
    df_2 = pd.read_csv(path_post, sep='\t', header=None)
    df_2.columns = ['y','nut']

    U_df['nut'] = df_2['nut']

    return tau,U_df


if __name__=='__main__':
    tau,U_df = get_wall('X1','down')
    print(U_df.head())
    plt.scatter(U_df['y'],U_df['Ux'])
    plt.xscale('log')
    plt.show()

