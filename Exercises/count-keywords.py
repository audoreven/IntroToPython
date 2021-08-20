import keyword

# getting list of keywords
key_words = keyword.kwlist

# initializing dictionary
count = {}

# getting file name
source = input("Enter a filename: ")

while True:
    try:
        file = open(source, "r")
        break
    except FileNotFoundError:
        print('File does not exist. Please try again. \n')
        source = input("Enter a filename: ")

# reading the file
lines = file.readlines()

# counting occurrences of keywords
for l in lines:
    words = l.split()
    for word in words:
        if word in key_words:
            if word in count:
                count[word] += 1
            else:
                count[word] = 1

# print results
print("Key Words \t Occurrences")
for kw in count.keys():
    if count[kw] > 0:
        print("{:12} {:<7}".format(kw, count[kw]))

