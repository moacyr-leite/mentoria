import json

def read_data(file_name) -> list:
    data = []
    with open(f"{file_name}.json", "r", encoding="utf-8") as f_data:
        data = json.load(f_data)
    return data

def white_data(file_name, data):
    with open(f"{file_name}.json", "w", encoding="utf-8") as f_data:
        json.dump(data, f_data, indent=4, ensure_ascii=False)
