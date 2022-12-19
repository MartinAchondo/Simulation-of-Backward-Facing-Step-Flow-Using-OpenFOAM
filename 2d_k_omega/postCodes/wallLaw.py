import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

endTime = 100
nu = 10.0**-6

path_case = os.getcwd()

def get_wall(X,wall):
    path_post = os.path.join(path_case,'postProcessing','shearStressWall',str(endTime),f'{X}_{wall}_wallShearStress.xy')

    tau_df = pd.read_csv(path_post, sep='\t', header=None)
    tau = abs(float(tau_df[1]))

    path_post = os.path.join(path_case,'postProcessing','wallLaw_U',str(endTime),f'{X}_{wall}_U.xy')
    U_df = pd.read_csv(path_post, sep='\t', header=None)
    U_df.columns = ['y','Ux','Uy','Uz']
    U_df.drop('Uy', inplace=True, axis=1)
    U_df.drop('Uz', inplace=True, axis=1)

    U_df['y'] = U_df['y']*np.sqrt(tau)/nu
    U_df['Ux'] = U_df['Ux']/np.sqrt(tau)

    return tau,U_df


if __name__=='__main__':
    tau,U_df = get_wall('X1','down')
    print(U_df.head())
    plt.scatter(U_df['y'],U_df['Ux'])
    plt.xscale('log')
    plt.show()

