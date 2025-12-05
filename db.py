import csv
import os

FILENAME = "money.txt"

def read_money():
	if not os.path.exists(FILENAME):
		return 100.0

	try:
		with open(FILENAME, "r", newline"") as file:
			reader = csv.reader(file)
			row = next(reader, None)
			if row:
				return float(row[0])
			else:
				return 100.0
	except Exception:
		return 100.0

def money_to_txt(amount):
	try: 
		with open(FILENAME, "w", newline="") as file:
			writer = csv.writer(file)
			writer.writerow([round(amount,2)])
	except Exception as e:
		print("error writing file:", e)
