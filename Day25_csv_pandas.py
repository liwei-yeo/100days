import pandas

data = pandas.read_csv("./Day25_2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

colour_series = data["Primary Fur Color"]
colour_list = colour_series.unique().tolist()
del colour_list[0]
squirrel_dict = {
    "Fur Color": [],
    "Count": [],
}

for colour in colour_list:
    squirrel_dict["Fur Color"].append(colour)
    # squirrel_dict["Count"].append(data["Primary Fur Color"] == colour.count())
    # print(type(data["Primary Fur Color"] == colour.count()))
    squirrel_dict["Count"].append(colour_series[data["Primary Fur Color"] == colour].count())

output = pandas.DataFrame(squirrel_dict)
output.to_csv("./Day25_squirrel_output.csv")


# with open("./Day25_weather_data.csv") as file:
#     data = file.readlines()
# print(data)

# import csv
# with open("./Day25_weather_data.csv") as file:
#     data = csv.reader(file)
#     mess_list = []
#     for row in data:
#         mess_list.append(row)
# temperatures = []
# for item in mess_list[1:]:
#     temperatures.append(int(item[1]))
#
# print(temperatures)

# import pandas
# data = pandas.read_csv("./Day25_weather_data.csv")
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].tolist()
# print(temp_list)

# average = sum(temp_list) / len(temp_list)
# average = data["temp"].mean()
# print(average)
# max = data["temp"].max()
# print(max)

# print(data["temp"])
# print(data.temp)

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# print(int(monday.temp)*9/5+32)

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores":[76, 56, 65],
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("./Day25_pandas.csv")
