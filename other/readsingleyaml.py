import yaml

file_name = "ex.yaml"

one_db = open(file_name, 'r')

db_info = yaml.load(one_db, Loader=yaml.Loader)

db_name = db_info["database"]["hiveName"]
for table in db_info["database"]["tables"]:
    print(f'{db_name},{table["hiveName"]}')

