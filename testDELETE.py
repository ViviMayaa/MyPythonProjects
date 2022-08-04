row1 = ["0️","⬜️","⬜️"]
row2 = ["1️","⬜️","⬜️"]
row3 = ["2️","⬜️","3️"]
map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
position = "23"
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
position1 = int(position[0] ) - 1
position2 = int(position[1] ) - 1

map[position2][position1] = 'x'

print(f"{row1}\n{row2}\n{row3}")