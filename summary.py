# demonstrating how separate parts of a function works
import csv
def read_rows(filename):
    with open(filename, encoding = "utf-8-sig") as f:
        return list(csv.DictReader(f))

def clean_values(rows, column):
    values = []
    for row in rows:
        value = row[column].strip()
        if value == "":
            continue
        values.append(float(value))
    return values


def summarize_values(values):
    if len(values) == 0:
        return {"Count": 0, "Smallest": None, "Largest": None, "Average": None}
    return {"Count": len(values), 
            "Smallest": min(values), 
            "Largest": max(values), 
            "Average": sum(values) / len(values)}


def summarize_all(filename, columns):
    rows = read_rows(filename)
    report = {}
    for column in columns:
        values = clean_values(rows, column)
        report[column] = summarize_values(values)

    return report
report = summarize_all("wards.csv", ["Pop", "area_km2"])

for column, stats in report.items():
    print(column, "->", stats)
   
        


rows = read_rows("wards.csv")
values = clean_values(rows, "Pop")
result = summarize_values(values)
print(result)