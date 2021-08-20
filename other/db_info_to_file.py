from os import listdir
from os.path import isfile, join
import yaml

path_to_folder = "../feed-db-conf"
yamlfiles = [f for f in listdir(path_to_folder) if isfile(join(path_to_folder, f))]

data_set = set()

for file in yamlfiles:
    if file.split('.')[-1] == "yaml":
        with open(path_to_folder+"/"+file, 'r') as db:
            try:
                db_info = yaml.load(db, Loader=yaml.Loader)

                db_name = db_info["database"]["hiveName"]
                for table in db_info["database"]["tables"]:
                    data_set.add(f'{db_name},{table["hiveName"]}\n')
            except yaml.YAMLError as exc:
                print(exc)

out_file = open('db_info.txt', 'w')

for d in sorted(data_set):
    out_file.write(d)

