import json
import pandas as pd
import os


def read_json(file_path):
    file = open(file_path)
    data = json.loads(file.read())
    data.pop('metadata')
    return data


def read_all_json_files(JSON_ROOT):
    files = os.listdir(JSON_ROOT)
    json_files = sorted([file for file in files if file.endswith(".json")])
    first = True
    for file in json_files:
        if first:
            json_contents = read_json(f"{JSON_ROOT}/{file}")
            df = pd.DataFrame(json_contents['results'])
            df['source']=file
            first = False
        else:
            json_contents = read_json(f"{JSON_ROOT}/{file}")
            temp = pd.DataFrame(json_contents['results'])
            temp['source']=file
            df = df.append(temp, ignore_index=True)
    return df
