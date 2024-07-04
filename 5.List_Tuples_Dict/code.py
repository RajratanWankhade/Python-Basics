# Tuple() vs List[] vs Set{} vs Dict{key:values} = cant modify.i.e.ADD or REMOVE from tuple, 
# Order doesnt matters in Set.

#Advance Set operations

friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}
local_friends = friends.difference(abroad)#remove elements from friends off the set abroad
print(local_friends)


friends_total = friends.union(abroad)
print(friends_total)


art_students = {"Bob","Jen","Rolf","Charlie"}
science_students = {"Bob","Jen","Adam","Anne"}

both = art_students.intersection(science_students)
total = art_students.union(science_students)

print(f"students studying both subjects: {both}")
print(f"total number of students: len{total}")