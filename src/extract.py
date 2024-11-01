import csv


# Read the CSV file and return a list of dictionaries
def read_csv(csv_file: str) -> list[str]:
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]
