# flooring calculator by Daniel Koman

import sys
sys.path.append("../lib") # add ../lib to system path to allow import of modules from lib folder (github data structure)

from prettytable import PrettyTable # import PrettyTable from prettytable library
from decimal import Decimal # use decimal.Decimal to avoid wonky python mathematics

class House:
	def __init__(self, name, sqFt, data):
		self.name = name
		self.sqFt = sqFt
		self.colorData = data

		self.colorCosts = {
		  "Red":Decimal(0.50),
		  "Orange":Decimal(0.51),
		  "Yellow":Decimal(0.52),
		  "Green":Decimal(0.53),
		  "Blue":Decimal(0.54),
		  "Cyan":Decimal(0.55),
		  "Purple":Decimal(0.56),
		  "White":Decimal(0.57),
		  "Black":Decimal(0.58),
		  "Brown":Decimal(0.59),
		  "Magenta":Decimal(0.60),
		  "Tan":Decimal(0.61),
		  "Olive":Decimal(0.62),
		  "Maroon":Decimal(0.63),
		  "Navy":Decimal(0.64),
		  "Aquamarine":Decimal(0.65),
		  "Turquoise":Decimal(0.66),
		  "Silver":Decimal(0.67),
		  "Lime":Decimal(0.68),
		  "Teal":Decimal(0.69),
		  "Indigo":Decimal(0.70),
		  "Violet":Decimal(0.71),
		  "Pink":Decimal(0.72),
		  "Gray":Decimal(0.73),
		  "Peach":Decimal(0.74),
		}
	
	def display(self):
		print(f"{self.name} will need a total of {self.sqFt} square feet of flooring material!") # print total square units needed
		print("Here's your shopping list:")
		totalCost = Decimal(0)
		for color in self.colorData: # iterate through colorData
			print(f"You will need {self.colorData[color]} square feet of {color},") # to print how much of each color is needed
			# catch keyerror exception here
			cost = Decimal(self.colorData[color] * self.colorCosts[color]) # multiply square feet by price per square foot
			print(f"costing ${cost} total.")
			totalCost += cost
		print(f"Total cost for flooring materials in {self.name} is ${totalCost}.")
			

print("Welcome to Flooring Calculator 1.0! Please enter a name for your house:")
houseName = input("House name? ")
houseName = houseName.title() # capitalize all first letters (titlecase)
print(f"Thanks! Please input each room name in {houseName}, followed by dimensions:")

roomData = [] # create a list to store room data
colorData = {} # create a dictionary to store running area totals of each color

squareFeet = 0 # zero square feet to begin
finished = False
while finished == False:
	roomName = input("Which room? ") # prompt user for room name
	if roomName == "": # if user hit enter at the room prompt without entering data
		done = input("Are you finished adding rooms? (Y or N)") # make sure user is done
		if done == "Y" or done == "y": # if confirmed,
			finished = True # we set finished to true to skip next loop iteration
		continue # restarting the loop will either end it (because finished == True), or begin from the start again
	roomName = roomName.title() # capitalize all first letters (titlecase)
	length = input("What is the length in feet? ") # prompt user for room length
	width = input("What is the width in feet? ") # prompt user for room width
	color = input(f"What color floor in {roomName}? ") # prompt user for floor color

	if length == "" or width == "" or color == "": # if user entered a room name but failed to enter data in any of the three subsequent fields,
		print("Please do not omit any room data. Let's try that again...") # complain to the user for having omitted data
		continue # we restart the loop

	color = color.title() # title case room color to avoid dictionary duplicates

	thisRoomArea = Decimal(length) * Decimal(width) # use decimal.Decimal to avoid wonky python mathematics

	roomData.append([roomName, length, width, thisRoomArea, color]) # add room data to list

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
table.title = houseName # use the house name as the table title
table.sortby = "Room" # sort the table object by room name
table.align = 'r' # right-align cell content
print(table) # print the table to the terminal

house = House(houseName, squareFeet, colorData)
house.display()

#print(house.colorData)



