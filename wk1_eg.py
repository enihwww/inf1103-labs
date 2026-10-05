print('Hello, World!')
print("Hello, World!")
print('He said, "Python is awesome!"')
print("It's a beautiful day!")
print('It\'s a "beautiful" day!')
print("It's a \"beautiful\" day!")
print(r'it\n1\t2')     # prints literally: it\n1\t2
print('it\n1\t2')       # \n and \t are interpreted

print(r"C:\Users\Name")   # literal backslashes preserved
print("C:\\Users\\Name")  # backslashes must be escaped to be interpreted literally

firstName = 'Yu'
print(firstName)
print(id(firstName))

first = 10
second = 20
first, second = second, first  # swap values
print(first)
print(second)
print(type(first))
print(type(second))

walk_circle = 0
for walk_circle in range(1, 10):
    if walk_circle == 5:
        continue
    print(walk_circle)
print("walking complete")
print(walk_circle)
