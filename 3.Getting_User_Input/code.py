name = input("Enter your name: ")
print("perfect")
print(".............................")

size_input = input(f"so, {name},how big is your house(in square feet)")
square_feet = int(size_input)
square_meters = square_feet / 10.8
print(f"{square_feet} square feet is {square_meters:.2f} sqr meter")# :.2f means rounding it to two points 
