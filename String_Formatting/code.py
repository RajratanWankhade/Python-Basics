#f-string

name = "Raj"
greeting = f"Hello, {name}"
print(greeting)


#template string with  .format()
name = "Ratan"
greeting_t = "Hello, {}".format(name)
print(greeting_t)

longer_phrase = "Hello, {}. Today is {}"
formatted = longer_phrase.format("Raj","Sunday")
print(formatted)


print("Hello, {}. Today is {}".format("Ratan","Monday"))