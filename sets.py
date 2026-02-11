#Set
thisset = {"apple", "banana", "cherry"}
print(thisset)

#Duplicates not allowed
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

#Get the length of a set
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

#Set items - Data Types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)

#type()
myset = {"apple", "banana", "cherry"}
print(type(myset))

#The set() Constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

#Access Items
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#Add Items
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#add sets
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#add any iterable
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

#remove item
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

#loop items
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#union
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#Join Multiple Sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

#Join a set and a tuple
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

#update
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#intersection
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

#Difference
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)

#Symmetric Differences
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)

#Creating a frozenset
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))


