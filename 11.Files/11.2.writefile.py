f='C:\\my backup\\Programming\\JALA Python\\11.Files\\WRITEME.txt'
t=input("Enter text to write to file: ")

with open(f, 'w') as fl:
    fl.write(t)
