# flooring calculator by Daniel Koman

from prettytable import PrettyTable
from decimal import Decimal # use decimal.Decimal to avoid wonky python mathematics

print("Welcome to Flooring Calculator 1.0! Please enter a name for your house:")
house = input("House name? ")
house = house.title() # capitalize all first letters (titlecase)
print(f"Thanks! Please input each room name in {house}, followed by dimensions:")

table = PrettyTable() # instantiate a new table object

table.field_names = ['Room', 'Length', 'Width', 'SqFt'] # set table field names

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

	if length == "" or width == "": # if user entered a room name but failed to enter data in any of the three subsequent fields,
		continue # we restart the loop

	thisRoomArea = Decimal(length) * Decimal(width) # use decimal.Decimal to avoid wonky python mathematics
	squareFeet += thisRoomArea # add current room area to running total
	table.add_row([room, length, width, thisRoomArea]) # add the data to the table
	 

table.title = house # use the house name as the table title
table.sortby = "Room" # sort the table object by room name
table.align = 'r' # right-align cell content

print(table) # print the table to the terminal
print(f"You will need a total of {squareFeet} square feet of flooring material!") # print total square units needed 
