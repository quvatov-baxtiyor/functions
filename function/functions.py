import csv

def csv_reader():
    with open("file/my_data.csv", "r",newline="") as f:
        reader = csv.reader(f)

        for row in reader:
            print(row)

def csv_write():
    with open("file/my_data.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Hey group 305"])

def add_csv():
    with open("file/my_data.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Hey group 305"])

def change_csv():
    pass

