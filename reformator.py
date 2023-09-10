from os import system
file = 'program'
command = f"pyuic5 {file}.ui -o {file}.py"
system(command)