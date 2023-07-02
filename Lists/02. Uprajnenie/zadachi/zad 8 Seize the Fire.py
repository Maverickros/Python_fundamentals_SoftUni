# The group of adventurists has gone on their first task. Now they should walk through fire - literally. They should use all
# the water they have left. Your task is to help them survive.
# Create a program that calculates the water needed to put out a "fire cell", based on the given information about its
# "fire level" and how much it gets affected by water.
# First, you will be given the level of fire inside the cell with the integer value of the cell, which represents the needed
# water to put out the fire. They will be given in the following format:
# "{typeOfFire} = {valueOfCell}#{typeOfFire} = {valueOfCell}# … {typeOfFire} =
# {valueOfCell}"
# Afterward you will receive the amount of water you have for putting out the fires. There is a range of fire for each
#fire type, and if a cell's value is below or exceeds it, it is invalid, and you do not need to put it out.
#                                          Type of Fire        Range
#                                          High               81 - 125
#                                          Medium             51 - 80
#                                          Low                 1 - 50
# If a cell is valid, you should put it out by reducing the water with its value. Putting out fire also takes effort, and you
# need to calculate it. Its value is equal to 25% of the cell's value. In the end, you will have to print the total effort. Keep
# putting out cells until you run out of water. Skip it and try the next one if you do not have enough water to put out a
# given cell. In the end, print the cells you have put out in the following format:
# "Cells:
# - {cell1}
# - {cell2}
# …
# - {cellN}"
# "Effort: {effort}"
# The effort should be formatted to the second decimal place.
# In the end, print the total fire you have put out from all the cells in the following format:
# "Total Fire: {total_fire}"

cells = input().split("#")
amount_of_water = int(input())
total_fire = 0
total_effort = 0
# правя един лист в който да съхранявам клетките
fire_out_cells = []
# определчм диапазоните
high = range(81, 125 + 1)
medium = range(51, 80 + 1)
low = range( 1, 50 + 1)
# определям клетките cell с фор цикъл
for cell in cells:
    # разделяме ги с интервал
    type_of_fire, cell_value = cell.split(" = ")
    cell_value = int(cell_value)
    # проверява дали клетката е валидна, дали е в диапазоните
    cell_is_valid = False
    # правя проверка за type of fire
    if type_of_fire == "High":
        if cell_value in high: # диапазона
            cell_is_valid = True
    elif type_of_fire == "Medium":
        if cell_value in medium:  # диапазона
            cell_is_valid = True
    elif type_of_fire == "Low":
        if cell_value in low:  # диапазона
            cell_is_valid = True
    # ако клетката е валидна и е в диапазоните , се опитваме да я гасим
    if cell_is_valid:
        # ако имам достатъчно вода
        if amount_of_water >= cell_value:
            # намалявам стойността на водата с толкова колкото е клетката,защото успявам да я загася
            amount_of_water -= cell_value
            # към fire out list добавям стойността на клетката
            fire_out_cells.append(cell_value)
            # увеличавам стойностите на
            total_fire += cell_value
            total_effort += cell_value * 0.25   # 25%
print('Cells:')
for fire_out_cell in fire_out_cells:
    print(f'- {fire_out_cell}')
print(f'Effort: {total_effort:.2f}')
print(f'Total Fire: {total_fire}')
