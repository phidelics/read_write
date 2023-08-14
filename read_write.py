## writing a csv
import csv
import pandas as pd

data = {
    "Name": ["Temi", "Igwemba", "Phanuel", "Theo", "Ibukun", "Victor", "Daniel", "Amusan", "Tolu"],
    "Age": [30, 33, 16, 40, 23, 34, 30, 35, 22],
    "Height": ["160cm", "162cm", "163cm", "165cm", "167cm", "170cm", "172cm", "174cm", "180cm"],
    "State": ["Lagos", "Anambra", "Kaduna", "Maiduguri", "Oyo", "Kogi", "Kwara", "Lagos","Ekiti"]
}
data = pd.DataFrame(data)
data.to_csv("file.csv", index= False)

print(data.head())


# Reading csv

df = pd.read_csv("file.csv")

print(df)