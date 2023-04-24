import pandas
gray_squirl = 0
cinnamon_squirl = 0
black_squirl = 0
squirrel_data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
# Gray, Cinnamon, Black
color_list = squirrel_data['Primary Fur Color']
for color in color_list:
    if color == 'Gray':
        gray_squirl += 1
    if color == "Cinnamon":
        cinnamon_squirl += 1
    if color == "Black":
        black_squirl += 1

total_dict = {
            'Fur color': ["Gray", "Cinnamon", "Black"],
            'Count': [gray_squirl, cinnamon_squirl, black_squirl]
              }
total_framed = pandas.DataFrame(total_dict)
print(total_framed)
