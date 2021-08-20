def replace_string(tar, old, new):
    """
    Replaces a string with another string
    :param tar: targeted string
    :param old: old string to be replaced
    :param new: new string to replace the old string with
    :return: new version of targeted string that replaced all instances of old with new
    """
    window_size = len(old)
    if tar == old:
        return new
    for i in range(len(tar)-window_size):
        if tar[i:window_size+i] == old:
            tar = tar[:i] + new + tar[window_size+i:]
    return tar


source = input("Enter a filename: ")

while True:
    try:
        file = open(source, "r")
        break
    except FileNotFoundError:
        print('File does not exist. Please try again. \n')
        source = input("Enter a filename: ")

old_str = input("Enter the old string to be replaced: ")
new_str = input("Enter the new string to replace the old string: ")

lines = file.readlines()

file.close()
file = open(source, 'w')

for l in lines:
    if old_str in l:
        l = replace_string(l, old_str, new_str)
    file.write(l)
print("\nString successfully replaced.")

