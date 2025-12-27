
row1= ["⬜️","️⬜️","️⬜️"]
row2= ["⬜️","️⬜️","️⬜️"]
row3= ["⬜️","️⬜️","️⬜️"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")
position = int(input("Where do you want to put the treasure? "))

first_position = position // 10
second_position = position % 10

map[first_position -1][second_position-1] = "X"

print(f"{row1}\n{row2}\n{row3}")

