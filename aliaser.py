# a simple aliaser for Apex RP
'''
To-do MBs:
add in google drive integration
add in ui elements
add in direct to bank integration
'''

def Aliaser():
    
    alias_name = input('''
Please enter the desired alias name
''')

    file_name =  "Alias.txt"

    #loops through and reads the file
    model_file = open(file_name, 'r')
    lines = []
    for line in model_file:
        if line == "" or line == "\n":
            None
        else:
            line = line.rstrip('\n')
            line = line.rstrip(";")
            lines.append(line)
    model_file.close()

    #loops thru and makes aliases
    for i, line in enumerate(lines):
        if i == 0:
            local_first_line = 'alias create ' + alias_name + ' ' + line + ';'
            local_first_line += alias_name + '1'
            print(local_first_line)
        elif line == "":
            print('\n')
        elif i == len(lines)-1:
            local_line = 'alias create ' + alias_name + str(i)
            print(local_line, line)
        else:
            local_line = 'alias create ' + alias_name + str(i)
            local_line += ' ' + line
            local_line += ';' + alias_name + str(i+1)
            print(local_line)
        print('\n')

    ending_msg = '''
Your alias has been created.
Please type in "CLOSE" to exit the program.
Else, type in any message to restart the program!
'''
    close = input(ending_msg)

    if close != "CLOSE":
        Aliaser()
    else:
        return


Aliaser()   # runs the program xd




    