import json

def read_json_data():
    # Read the test data from the JSON file
    with open("TestData/testdata.json") as file:
        data = json.load(file)
    return data