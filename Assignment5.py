a = int(input("Enter first number for list: "))
b = int(input("Enter Second number for list: "))
c = int(input("Enter Third number for list: "))
d = int(input("Enter Fourth number for list: "))
e = int(input("Enter fifth number for list: "))

# Sum of elements
lst = [a,b,c,d,e]
print(lst)
print(sum(lst))
 
# Smallest number
print("Smallest number in list: ",min(lst))

# Largest number
print("Largest Number in list: ",max(lst))

# Ascending order
lst.sort()
print("List in Ascending order: ",lst)

# Descending order
lst.sort(reverse=True)
print("List in Descending order",lst)

# To tuple
n = ()
n = tuple(lst)
print(n)

# Deleting the list
del lst

