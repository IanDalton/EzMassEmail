import csv
with open("table_0.csv", "r",encoding="utf-8") as f:
    reader = csv.reader(f)
    numeros = []
    for row in reader:
        for column in row:
            numeros.append(column) if column.isnumeric() else None

print(numeros)