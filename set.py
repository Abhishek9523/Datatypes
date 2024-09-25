print("------------------------------set()---------------------------------")
my_data = {10,20,30,20,30,40,30}
print(set(my_data))
print(type(my_data))

my_data1 = {"Abhishek",20,30,20,30,"Rahul",30}
print(set(my_data1))
print(type(my_data1))

# Frozen sets are immutable, meaning that their elements cannot be changed after they have been created.
print("-----------frozenset()----------------")
my_data2 = {10,20,"Abhishek",20,"Rahul",30,"Raj",40}
print(set(my_data2))
print(frozenset(my_data2))


# O/P:
# print("-----------------------------set()---------------------------------")
# {40, 10, 20, 30}
# <class 'set'>
# my_data3 = {'Abhishek', 20, 30, 'Rahul'}
# <class 'set'>
# print("-----------frozenset()----------------")
# {20, 'Rahul', 40, 10, 'Abhishek', 'Raj', 30}
# frozenset({20, 'Rahul', 40, 10, 'Abhishek', 'Raj', 30})

