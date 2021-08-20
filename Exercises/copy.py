source = input("Enter source file: ")

while True:
    try:
        file = open(source, "r")
        break
    except FileNotFoundError:
        print('File does not exist. Please try again. \n')
        source = input("Enter source file: ")

target = input("Enter the target file: ")

upper_file = open(target, "w")

lines = file.read()

for l in lines:
    upper_file.write(l.upper())

print("\nFile has been written: '"+target+"'")