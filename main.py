import json

def read_json():
    path = 'files/test_files/hw.json'
    with open(path, encoding='utf-8') as json_file:
	    data = json.load(json_file)

    return data

if __name__ == '__main__':
    print(read_json())
