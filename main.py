#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

#First application

print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))

#can use any percentage of tip now instead of the limited options
tip = int(input("how much tip would you like to give? "))

total_bill = (tip/100 * bill) + bill

people = int(input("How many people to split the bill? "))

#used the .2f format to get the bill in 2 decimal values always
bill_per_person = "{:.2f}".format(total_bill/people)
print(f"Each person should pay: ${bill_per_person}")
