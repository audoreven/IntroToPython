db_table_list = set()
db_table_used = set()

file1 = "full_db_table.csv"
file2 = "complete_db_info.txt"

try:
    all_tables = open(file1, "r")
    used_tables = open(file2, "r")
except FileNotFoundError:
    print('File does not exist. Please try again. \n')

f1_lines = all_tables.readlines()
f2_lines = used_tables.readlines()

# process file 1:
db_to_table_info = set()
for l in f1_lines:
    db_to_table_info.add(l.split('/')[-1])

# process to string
for table in db_to_table_info:
    separate = table.split(',')
    db_table_list.add(f'{separate[0].split("=")[-1]},{separate[1].split("=")[-1]}')

# process used databases
for l in f2_lines:
    db_table_used.add(l)

#output
outfile = open('unused_tables.txt', 'w')
for table in sorted(db_table_used.difference(db_table_list)):
    outfile.write(table)


outfile2 = open('used_tables.txt', 'w')
left_outer_set = db_table_used.difference(db_table_list)
for table in sorted(db_table_list.difference(left_outer_set)):
    outfile2.write(table)

print(sorted(db_table_list))
print(sorted(db_table_used))