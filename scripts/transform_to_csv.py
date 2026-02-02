import json
import csv
from datetime import datetime

def calculate_cycle_time(submission, approval):
    if not approval:
        return None
    sub_date = datetime.strptime(submission, "%Y-%m-%d")
    app_date = datetime.strptime(approval, "%Y-%m-%d")
    return (app_date - sub_date).days

with open('../data/pmis_mock_data.json', 'r') as json_file:
    data = json.load(json_file)

with open('../data/pmis_output.csv', 'w', newline='') as csv_file:
    fieldnames = ['document_id', 'discipline', 'status', 'cycle_time_days']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    for item in data:
        writer.writerow({
            'document_id': item['document_id'],
            'discipline': item['discipline'],
            'status': item['status'],
            'cycle_time_days': calculate_cycle_time(
                item['submission_date'],
                item['approval_date']
            )
        })

print("PMIS data transformed and exported to CSV")
