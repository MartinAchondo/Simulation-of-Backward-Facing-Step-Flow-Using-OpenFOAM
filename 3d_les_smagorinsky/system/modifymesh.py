import os


file_name = 'boundary'
path_current_L = os.path.dirname(os.path.realpath(__file__)).split("\\")
path_current_L.pop()
path_current = "\\".join(path_current_L)

path_file = os.path.join(path_current,'constant','polyMesh',file_name)




text1 = '''    fixedWalls
    {
        type            patch;'''

text2 = '''    fixedWalls
    {
        type            wall;'''

##         inGroups        List<word> 1(empty);

with open(path_file, 'r') as f:
    content = f.read()
    content = content.replace(text1,text2)


with open(path_file, 'w') as file:
    file.write(content)
  

print("polyMesh OK\n\n")