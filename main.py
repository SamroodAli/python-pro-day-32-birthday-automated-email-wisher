import pandas

data = pandas.read_csv("birthdays.csv").to_dict(orient="records")
print(data)
