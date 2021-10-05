# flooring calculator by Daniel Koman

import sys
sys.path.append("../lib") # add ../lib to system path to allow import of modules from lib folder (github data structure)

from prettytable import PrettyTable # import PrettyTable from prettytable library
from decimal import Decimal # use decimal.Decimal to avoid wonky python mathematics

print("Welcome to Flooring Calculator 1.0! Please enter a name for your house:")
house = input("House name? ")
house = house.title() # capitalize all first letters (titlecase)
print(f"Thanks! Please input each room name in {house}, followed by dimensions:")

roomData = [] # create a list to store room data
colorData = {} # create a dictionary to store running area totals of each color

squareFeet = 0 # zero square feet to begin
finished = False
while finished == False:
	room = input("Which room? ") # prompt user for room name
	if room == "": # if user hit enter at the room prompt without entering data
		done = input("Are you finished adding rooms? (Y or N)") # make sure user is done
		if done == "Y" or done == "y": # if confirmed,
			finished = True # we set finished to true to skip next loop iteration
		continue # restarting the loop will either end it (because finished == True), or begin from the start again
	room = room.title() # capitalize all first letters (titlecase)
	length = input("What is the length in feet? ") # prompt user for room length
	width = input("What is the width in feet? ") # prompt user for room width
	color = input(f"What color floor in {room}? ") # prompt user for floor color

	if length == "" or width == "" or color == "": # if user entered a room name but failed to enter data in any of the three subsequent fields,
		print("Please do not omit any room data. Let's try that again...") # complain to the user for having omitted data
		continue # we restart the loop

	color = color.title() # title case room color to avoid dictionary duplicates

	thisRoomArea = Decimal(length) * Decimal(width) # use decimal.Decimal to avoid wonky python mathematics

	roomData.append([room, length, width, thisRoomArea, color]) # add room data to list

	if color in colorData: # check first to see if color key already exists in dictionary
		colorData[color] += thisRoomArea # add square feet of this color to dictionary total
	else:
		colorData[color] = thisRoomArea # create new key with new color

# table stuff
table = PrettyTable() # instantiate a new table object
table.field_names = ['Room', 'Length', 'Width', 'SqFt', 'Color'] # set table field names
for room in roomData: # iterate through list to add table entries and calculate total area
	squareFeet += room[3] # add squareFeet to running total
	table.add_row(room) # add room data to the table
table.title = house # use the house name as the table title
table.sortby = "Room" # sort the table object by room name
table.align = 'r' # right-align cell content
print(table) # print the table to the terminal

for color in colorData: # iterate through colorData
	print(f"You will need {colorData[color]} square feet of {color}.") # to print how much of each color is needed
print(f"You will need a total of {squareFeet} square feet of flooring material!") # print total square units needed

