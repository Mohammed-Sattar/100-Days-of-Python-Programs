import csv
import pandas

# Challenge: Reading from weather_data.csv to a list
# with open(r"Day 25 - Intermediate - CSV Files\weather_data.csv") as csv_file:
#     data = csv_file.readlines()
#     print(data)


# A better way to read csv files using Python's built-in library
# with open(r"Day 25 - Intermediate - CSV Files\weather_data.csv") as csv_file:
#     data = csv.reader(csv_file)
#     temperatures = []
#     count = 0
#     for row in data:
#         print(f"{row}")

#         if count != 0:
#             temperatures.append(int(row[1]))

#         count += 1
    
#     print(temperatures)


# An even better way to read csv files using Pandas library, allows complex filtering and manipulation
# data = pandas.read_csv(r"Day 25 - Intermediate - CSV Files\weather_data.csv")
# print(type(data))

# Getting data in specific columns:
# print(data["temp"])
# Alternative way to access a specific column of data, instead of accessing as a dict it can be accessed as if it were and attribute
# print(data.temp)

# Converting table to a dictionary where each row is a list corresponding to a certain key
# data_dict = data.to_dict()
# print(data_dict)

# Converting a specific row to a list
# temp_list = data["temp"].to_list()
# print(temp_list)

# Operations on a row
# print(data["temp"].mean())
# print(data["temp"].max())

# Getting data in specific rows:
# print(f"{data[data.day == "Monday"]}\n")
# print(f"{data[data.temp == data.temp.max()]}\n")

# monday = data[data.day == "Monday"]
# # print(monday["condition"])

# day_temp = data[data.temp == data.temp.max()]
# max_temp_value = int(day_temp.temp.iloc[0])

# monday_temp = monday.temp[0]

# fahrenheit = (monday_temp * 9/5) + 32
# print(f"{fahrenheit}")


data_dict = {
    "Names": ["John", "Jim", "James"],
    "Scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv(r"Day 25 - Intermediate - CSV Files\score_data.csv")