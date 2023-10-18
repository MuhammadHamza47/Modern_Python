# name : str = "Muhammad Hamza"
# print(name)

# name1 : list[str] = ['a', 'b', 'c', 'd', 'e', 'f']
# print(name1)
# print(type(name1))
# print(id(name1))
# print([i for i in dir(name1) if "__" not in i])


name : tuple[str, int, float] = ('a', 234, 23435.5)
print(name)
print(type(name))
print(id(name))
print([i for i in dir(name) if "__" not in i])