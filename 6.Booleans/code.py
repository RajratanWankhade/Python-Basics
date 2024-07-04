# operations: ==, !=, >, < , >=, <=.
movies = {"Godfather","Her","Green Book"}
user_movie = input("what movie you watched recently: ")
if user_movie in movies:
    print(f"I have watched {user_movie} too!")
else:
    print("oh i missed that movie")    

print("..................................................")
print(" MAGIC NUMBER APP")

number = 7
user_input = input("Enter 'y' if you would like to play: ")

if user_input == "y":
    user_number = int(input("Guess the number: "))
    if user_number == number:
        print("Bingo, its correct")
    else:
        print("try again")    



