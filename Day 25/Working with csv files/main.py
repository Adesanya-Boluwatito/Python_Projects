import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])


data_dict = data.to_dict()
print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# #workin wit t
# print(data["condition"])
# print(data.condition)

# print(data[data.day == "Monday"])
# top_temp = (data["temp"].max())
# print(data[data.temp == top_temp])
#
# monday = data[data.day == "Monday"]
# temp = int(monday.temp) * 1.8 + 32
# print(temp)

#create dataframes from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "score": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

print(grey_squirrel_count)
print(red_squirrel_count)
print(black_squirrel_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrel_count, red_squirrel_count, black_squirrel_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("Squirrel_count.csv")
