# CY83R-3X71NC710N
# Homework Time Calculator


homeworklist = []

# Enter the name of each homework assignment and adds to the list until the user types done.

homework = "Enter the name of each homework assignment you have to do."
print("Enter 'done' when finished.")
print("----------------------------")

while not homework == 'done':
    homework = input("> ")
    homeworklist.append(homework)

print("----------------------------")

# Calculate time that it will take for each assignment

# Sanitize input to prevent user from putting in invalid characters

timetaken = 0
print("How many minutes will it take to work on each assignment?")
for item in homeworklist:
    userinput = input(item + ": ")
    while not userinput.isnumeric():
        userinput = input(item + ": ")
    timetaken = timetaken + float(userinput)

print("----------------------------")

print("It will take you",timetaken,"minutes to complete your homework.")
