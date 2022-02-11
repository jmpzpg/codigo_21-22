def only_ints(v1, v2):
    return type(v1) == type(v2) == int

print(only_ints(1,2))
print(only_ints('a',1))