class FileNotFound(FileExistsError):
    def __init__(self, file_name):
        self.filename = file_name

    def __str__(self):
        return "'"+self.filename+"' was not found. Please try again."


def open_file(file_name):
    try:
        filehand = open(file_name, 'r')
    except FileNotFoundError:
        try:
            raise FileNotFound(file_name)
        except FileNotFound as e:
            print(e)


# open_file("main.p")


letter_map = {'a': 1, 'c': 1, 't': 1}
letter_map_2 = {'a': 1, 'c': 1, 't': 1}

letter_maps = [{'a': 1, 'c': 1, 't': 1}, {'a': 1, 'c': 1, 't': 1}]

print(letter_maps[0] == letter_maps[1])


l = [1,2,3,4,5]

l+=[1,2,3,4]

print(l)