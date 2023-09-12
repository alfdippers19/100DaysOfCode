print("Welcome to the tip calculator.")

#Takes in sub total bill and stores it as a floating point number
subtotal_bill = float(input("What was the total bill? $"))

#Takes in an intager to be converted later into a multiplier-
#-to calculate the full bill
percent_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

#Takes in an intager that will split the total bill equally
ways_split = int(input("How many people to split the bill? "))

#Converts percentage into multiplier
multiplier = (percent_tip / 100) + 1

#Calculates the full amount owed
total_bill = (subtotal_bill * multiplier)

#Calculates what each person should owe; rounded to 2 decimal places
per_person = round((total_bill / ways_split),2)

#Prints what each person owes
print(f"Each person should pay ${per_person}")

#If the values in chronological order $124.56, 12, 7
#The final value is $19.93