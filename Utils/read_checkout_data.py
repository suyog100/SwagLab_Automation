import csv

def read_checkout_data(file_path):
    with open(file_path, newline='') as csvfile:
        data = list(csv.DictReader(csvfile))
    return data
