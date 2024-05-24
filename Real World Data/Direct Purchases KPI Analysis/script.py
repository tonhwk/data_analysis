import csv

# Open the input CSV file with semicolon delimiter
with open('daikin_purchase_orders.csv', 'r', newline='', encoding='utf-8') as infile:
    reader = csv.reader(infile, delimiter=';')
    data = list(reader)

# Open the output CSV file with comma delimiter
with open('output_daikin.csv', 'w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(data)

print("CSV file converted successfully from semicolon to comma delimiter.")