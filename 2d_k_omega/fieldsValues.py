
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

\\*---------------------------------------------------------------------------*/\n\n\n'''

class foamCase():

    def __init__(self) -> None:
        
        self.Re = 7000
        self.H = 0.2
        self.h = 0.1
<<<<<<< HEAD
=======
        self.L = 2.0

>>>>>>> cc37e1a (modifications)
        self.nu = 10.0**-6
        self.rho = 10.0**3
        
        self.calculate_fields()

        self.endTime = 1000
 
    def calculate_fields(self):

        L = 0.07*self.h
        T = 0.05

        self.u = self.Re*self.nu/self.H

        self.k = 1.5*(self.u*T)**2
        self.epsilon = 0.09**0.75*self.k**1.5/L
        self.omega = self.epsilon/self.k

        self.adim_factor = 1.0/(0.5*self.u**2)
  

case = foamCase()


if __name__=='__main__':

    def modify_file(name,text):
        with open(os.path.join(file_path,name), 'w') as f:
            f.write(text)

    file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),'constant')

    name = 'initialConditions'

    text += f'U_inlet_ave   {case.u};\n'
    text += f'k_ave         {case.k};\n'
    text += f'omega_ave     {case.omega};\n'
    text += f'nu_input      {case.nu};\n'
    text += f'rho_input     {case.rho};\n'
    text += f'factor_adim   {case.adim_factor};\n'

    modify_file(name,text)

    print("Fields Values OK\n\n")