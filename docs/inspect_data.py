import csv

# with open("Places.csv", encoding="utf-8-sig") as f:
#     reader = csv.DictReader(f)
#     rows = list(reader)

# values = []
# for row in rows:
#     row = row['area_sqkm'].strip()
#     if row == "":
#         continue
#     values.append(float(row))

# print("largest value:", max(values))
# print("smallest value:", min(values))
# print("count:", len(values))

def inspect_column(filename, column):
    with open(filename, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    values = []
    for row in rows:
        raw = row[column].strip()
        if raw == "":
            continue
        values.append(float(raw))

    return{
        "smallest":min(values),
        "largest":max(values),
        "count": len(values)
    }

result_area = inspect_column("Places.csv", "area_sqkm")
print(result_area)