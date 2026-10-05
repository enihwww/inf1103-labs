#list indexing and slicing
mylist = ['abc', 123, True, [1, 2, 3], {'key': 'value'}, (4, 5), None]
print(mylist[0])  # Output: 'abc'
print(mylist[-1])  # Output: None
print(mylist[3][1])  # Output: 2
print(mylist[4]['key'])  # Output: 'value'
print(mylist[5][0])  # Output: 4
print(mylist[:])
print(mylist[::]) 
print(mylist[::-1]) 
print(mylist[-3:-1:-1])
print(mylist[-3:-1:1])   
print(mylist[-1:-3:-1])  
print("abc" in mylist)  # Output: True

#list operations
my_list = ['abc', 123, True, [0,1,2], 'fff', -1, -500]
print(my_list)
my_list[1] = 'efg'
print(my_list)
my_list.append('hij')
my_list.insert(0, 'klmn')
print(my_list)

del my_list[-2]
print(my_list)
my_list.remove(True)
print(my_list)
print(len(my_list))

#for loop
fruits = ["Apple", "Banana", "Orange"]

for fruit in fruits:
    print(fruit)

#deep copy and shallow copy
import copy

list1 = [[1, 2], [3, 4]]
list2 = copy.deepcopy(list1)
list2[0][0] = 99
print(list1)   # [[1, 2], [3, 4]]  <- unaffected, fully independent
print(list2)   # [[99, 2], [3, 4]]  <- modified, independent copy

#functions stored in a list
def add(x):
    return x + 10

def multiply(x):
    return x * 10

def square(x):
    return x ** 2

operations = [add, multiply, square]

print(operations[0](5))   # calls add(5) -> 15
print(operations[1](1))   # calls multiply(1) -> 10
print(operations[2](5))   # calls square(5) -> 25

#write data to a file
with open("orders.txt", "w") as file:
    file.write("1001,Wireless Mouse,2\n")
    file.write("1002,Keyboard,1\n")
    file.write("1003,USB Cable,3\n")

with open("orders.txt", "r") as file:
    for line in file:
        print(line.strip())

orders = [
    "1001,Wireless Mouse,2\n",
    "1002,Keyboard,1\n",
    "1003,USB Cable,3\n"
]
with open("orders.txt", "w") as file:
    file.writelines(orders)

with open("orders.txt", "r") as file:
    for line in file:
        print(line.strip())

#open a file and append data to it
with open("orders.txt", "a") as file:
    file.write("1004,Monitor,1\n")
    file.write("1005,Laptop Stand,2\n")

#append lines to a list from a file eg test.txt have apple, banana 
#output should be ['apple', 'banana']
my_list = []
with open("test.txt", "r") as file:
    for line in file:
        my_list.append(line.strip())

print(my_list)