import csv

with open("Places.csv", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

# long way
values = []
for row in rows:
    values.append(float(row["area_sqkm"]))
print("long way: ", values)

# short way
values = [float(row["area_sqkm"]) for row in rows]
print("short way ", values)