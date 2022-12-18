import os


file_name = 'boundary'
path_current_L = os.path.dirname(os.path.realpath(__file__)).split("\\")
path_current_L.pop()
path_current = "\\".join(path_current_L)

path_file = os.path.join(path_current,'constant','polyMesh',file_name)

frontAndBack_text1 = '''frontAndBack
    {
        type            patch;'''


frontAndBack_text2 = '''frontAndBack
    {
        type            empty;
        physicalType    empty;'''


fixedWalls_text1 = '''    fixedWalls
    {
        type            patch;'''

fixedWalls_text2 = '''    fixedWalls
    {
        type            wall;'''

##         inGroups        List<word> 1(empty);

with open(path_file, 'r') as f:
    content = f.read()
    content = content.replace(frontAndBack_text1,frontAndBack_text2)
    content = content.replace(fixedWalls_text1,fixedWalls_text2)



with open(path_file, 'w') as file:
  
    file.write(content)
  

print("polyMesh OK\n\n")
