#here we will practice on dictionaries and sets
#Dictionary

info = {
    "name" : "Asad",
    "semester" : "2nd",
    "department" : "CS",
    "CGPA" : 3.14
}

# # print(info)
# # print(info.keys())
# print(f"{info.keys()} {"these are keys"}")
# print(f"{info.values()} {"these are values"}")
# print(f"{info.items()} {"these are items"}")
# print(f"{info.get("semester")} {"get method"}")
subjects = {
    "subjects" : ["Maths", "ML"]
}
info.update(subjects)
print(info)

#set
# It is the collection of unordered items, each element in the set must be unique and immutable.

set = {1,2,3,4,5,6}
print(type(set))

set.add("world")
print(set)
set.remove("world")
print(set)
set.pop()
print(set)
set.clear()
print(set)
numbers = [1,2,3,4]
set.update(numbers)
print(set)