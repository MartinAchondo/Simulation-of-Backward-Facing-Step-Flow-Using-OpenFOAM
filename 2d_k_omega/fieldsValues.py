
import os

mod_line = 20
file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),'0')

Re = 8000
H = 0.2
h = 0.1
nu = 10**-6
rho = 10**3
L = 0.07*h

T = 0.05


u = Re*nu/H

k = 1.5*(u*T)**2
epsilon = 0.09**0.75*k**1.5/L
omega = epsilon/k

factor = 1/(0.5*u**2)


def modify_file(name,text,mod_line):
    with open(os.path.join(file_path,name), 'r') as f:
        content = f.read()
        content = content.split('\n')
        content[mod_line-1] = text
        content = '\n'.join(content)
    with open(os.path.join(file_path,name), 'w') as f:
        f.write(content)
  
name = 'U'
text = f'                const scalar U_inlet = {u};'
modify_file(name,text,56)

name = 'k'
text = f'internalField   uniform {k};'
modify_file(name,text,mod_line)

name = 'omega'
text = f'internalField   uniform {omega};'
modify_file(name,text,mod_line)



file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),'system')
mod_line = 18

name = 'controlDict'
text = f'scale_factor  {factor};'
modify_file(name,text,mod_line)


print("Fields Values OK\n\n")