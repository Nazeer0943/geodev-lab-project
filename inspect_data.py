import csv

def inspect_column(file_name, column):
    with open(file_name, encoding = "utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    values = []
    for row in rows:
        value = row[column]
        # I intentionally remove one value from the Pop column to test the continue concept below. This is to ensure that the code can handle missing values without crashing.
        if value == "":
            continue
        values.append(value)
    return {"Smallest": min(values), "Largest": max(values), "Count": len(values)}


pop_result = inspect_column("wards.csv", "Pop")
area_result = inspect_column("wards.csv", "area_km2")
print(area_result)
print(pop_result)
