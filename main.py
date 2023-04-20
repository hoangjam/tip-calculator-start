#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6


#Format the result to 2 decimal places = 33.60


#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
bill_amount = input("What is the bill amount? ")
tip_amount = input("What percentage tip would you like to give? 10, 12 or 15? ")
tip_amount_converted = 1 + (float(tip_amount) / 100)
# print(tip_amount_converted)

number_of_people = input("How many people are splitting the bill? ")

total = float(bill_amount) * (tip_amount_converted)
split = total / float(number_of_people)

print(f"The total bill is ${round(total, 2)} including tip")
print(f"Each person should pay ${round(split, 2)}")