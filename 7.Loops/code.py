number = 7

while True:
    user_input = input("Would you like to play? (Y/n) ")
    if user_input == "n":
        break
    user_number = int(input("Guess the number: "))
    if user_number == number:
        print("Bingo, its correct")
    else:
        print("try again")   


print(".............FOR      LOOP..............")

friends = ["Rolf","Jen","Bob","Anne"]
for friend in friends:
    print(f"{friend} is my Friend")

print(".......CALCULATE_AVERAGE_GRADE_USING_FOR_LOOP.......")

grades = [35, 67, 98, 100, 100]
total = 0
amount = len(grades)

for grade in grades:
    total += grade
print(total/amount)    

print("...................................")

numbers = [1,2,3,4,5,6,7,8,9]
evens = []

for number in numbers:
    if number % 2 == 0:
        evens.append(number)
print(evens)

 