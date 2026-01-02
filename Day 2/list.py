# """
# CRUD in List
# i)Updating at the end of the list
# ii)Altering the existing item

# i) Append
# marks = [10] or []
# marks.append(10)


# ii)altering the existing item
# marks = [10,20,30]
# marks[1] = 35

# iii) Delete
#  > Deleting by searching through value
#  names = ["John", "Alice", "Keisha", "Lan"]
#  names.remove("Alice")

#  > Deleting through index
#  names=["John", "Alice", "Keisha", "Lan"]
#  names.pop(2)

#  > Delete the list
#  del names

#  > Clear the list
#  names.clear()
# """

list1 = [10,20,30,40]

first_item = list1[0]
print(first_item)

list1.append(55)
print(list1)

list1[0]=90
print(list1)

#Delete 
# Deleting using value
names = ["John", "Alice"]
names.remove("John")
print(names)

# Deleting using index
names.append("Ram")
print(len(names))
names.pop(1)
print(names)

# clear the name
names.clear()
print(names)

#deleting the name
del names
# print(names)

names=("Aryan", "Aryan")
del names