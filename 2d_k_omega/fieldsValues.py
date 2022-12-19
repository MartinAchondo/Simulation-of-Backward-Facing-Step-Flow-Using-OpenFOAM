
import os

text = '''/*--------------------------------*- C++ -*----------------------------------*\\
  =========                 |
  \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox
   \\    /   O peration     | Website:  https://openfoam.org
    \\  /    A nd           | Version:  8
     \\/     M anipulation  |
---------------------------------------------------------------------------
Description
    Values of fields and properties.

\*---------------------------------------------------------------------------*/\n\n\n'''



file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),'constant')

Re = 8000
H = 0.2
h = 0.1
nu = 10.0**-6
rho = 10.0**3
L = 0.07*h

T = 0.05


u = Re*nu/H

k = 1.5*(u*T)**2
epsilon = 0.09**0.75*k**1.5/L
omega = epsilon/k

factor = 1/(0.5*u**2)


def modify_file(name,text):
    with open(os.path.join(file_path,name), 'w') as f:
        f.write(text)
  

name = 'initialConditions'

text += f'U_inlet_ave   {u};\n'
text += f'k_ave         {k};\n'
text += f'omega_ave     {omega};\n'
text += f'nu_input      {nu};\n'
text += f'rho_input     {rho};\n'
text += f'factor_adim   {factor};\n'

modify_file(name,text)

print("Fields Values OK\n\n")