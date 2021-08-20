db_list = set()
db_used = set()

file1 = "feed_db_size.csv"
file2 = "full_db_list.csv"

try:
    all_db = open(file1, "r")
    used_db = open(file2, "r")
except FileNotFoundError:
    print('File does not exist. Please try again. \n')

f1_lines = all_db.readlines()
f2_lines = used_db.readlines()

for l in f1_lines:
    db_list.add(l.split(',')[1].split('=')[-1])

for l in f2_lines:
    db_used.add(l.split(',')[2].split('=')[-1])

for db in sorted(db_list.difference(db_used)):
    print(db)

print(sorted(db_used))
print(sorted(db_list))
