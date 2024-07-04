#Lambda Function
def add(x,y):
    return x + y
print(add(3, 4))

add = lambda x, y: x + y
print(add(4,7))

number = [1,3,5,9]
doubled = print([x * 2 for x in number])

square = print(list(map(lambda x: x * 2, number )))


