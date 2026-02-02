import json

def extract_pmis_data():
    with open('../data/pmis_mock_data.json', 'r') as file:
        data = json.load(file)
    return data

if __name__ == "__main__":
    pmis_data = extract_pmis_data()
    print(f"Extracted {len(pmis_data)} PMIS records")
