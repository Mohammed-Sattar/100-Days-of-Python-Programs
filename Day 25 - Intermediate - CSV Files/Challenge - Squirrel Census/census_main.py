import pandas

data = pandas.read_csv(r"Day 25 - Intermediate - CSV Files\Challenge - Squirrel Census\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
color_col = data["Primary Fur Color"]

print(color_col.nunique()) # prints the number of unique colors in the column, in this case there are 3 unique squirrel colors


color_count = color_col.value_counts() # counts the number of occurrences for each unique element
squirrel_count = color_count.to_csv(r"Day 25 - Intermediate - CSV Files\Challenge - Squirrel Census\squirrel_count.csv")
print(color_count)