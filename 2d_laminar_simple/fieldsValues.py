
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
        
        self.Re = 800
        self.H = 0.2
        self.h = 0.1
<<<<<<< HEAD
        self.L = 2.7

=======
>>>>>>> ea60bfa93e61337fec420f36a047d8654fa0de64
        self.nu = 10.0**-6
        self.rho = 10.0**3
        
        self.calculate_fields()
<<<<<<< HEAD
=======

        self.endTime = 1000
>>>>>>> ea60bfa93e61337fec420f36a047d8654fa0de64
 
    def calculate_fields(self):

        self.u = self.Re*self.nu/self.H

        self.adim_factor = 1.0/(0.5*self.u**2)
  

case = foamCase()


if __name__=='__main__':

    def modify_file(name,text):
        with open(os.path.join(file_path,name), 'w') as f:
            f.write(text)

    file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),'constant')

<<<<<<< HEAD
    name = 'fieldsValues'
=======
    name = 'initialConditions'
>>>>>>> ea60bfa93e61337fec420f36a047d8654fa0de64

    text += f'U_inlet_ave   {case.u};\n'
    text += f'nu_input      {case.nu};\n'
    text += f'rho_input     {case.rho};\n'
    text += f'factor_adim   {case.adim_factor};\n'
<<<<<<< HEAD
    text += f'Lx   {case.L};\n'
    #text += f'endTime_input   {case.endTime};\n'
=======
>>>>>>> ea60bfa93e61337fec420f36a047d8654fa0de64

    modify_file(name,text)

    print("Fields Values OK\n\n")