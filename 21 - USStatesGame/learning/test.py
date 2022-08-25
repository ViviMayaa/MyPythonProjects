import csv
import pandas
# weather_data_list = []
# temperature_list = []
# temperature_list_int = []
# with open("./weather_data.csv") as weather_data:
#     weather_data_list = csv.reader(weather_data)
#     for line in weather_data_list:
#         temperature_list.append(line[1])
#         print(line)
#
# temperature_list.remove(temperature_list[0])
# for value in temperature_list:
#     temperature_list_int.append(int(value))
#
# print(f"temperature : {temperature_list_int}")

data = pandas.read_csv("weather_data.csv")
data_list = data["temp"].to_list()
total_temp = 0
# total_temp = [total_temp ++ element for element in data_list]

# average_temp = sum(data_list) / len(data_list)
# print(average_temp)
# print(data['temp'].mean())
# print(data.temp)

# get data in a row
# print(data[data.day == "Monday"])
# print(data[data.temp == data['temp'].max()])

# fahrenheit = (celsius * 1.8) + 32
# monday = (data[data.day == 'Monday'])
# print((monday.temp * 1.8) + 32)

# creating dataframe from scrath
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)
# create csv file
data.to_csv("new_data.csv")
