import os

path = os.getcwd()+"\\..\\CH7\\phoneAndEmail.py"
#print(os.path.split(path))
#print(os.path.getsize(path))
file = open(path)
print(file.readlines())
