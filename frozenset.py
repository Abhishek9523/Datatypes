# my_list=[2,4,6,8,10,15,20]
# my_list=[10,20,30,40,50,60]
# my_tuple=(1,3,5,8,12,6,15,22)
# my_set={22,24,52,45,65,75,'rahul'}
# my_dict={'name':'abhishek','quali':'BCA'}

# print(frozenset(my_list))
# print(frozenset(my_tuple))
# print(frozenset(my_set))
# print(frozenset(my_dict))

# # inbuilt function
# print(min(my_list))
# print(max(my_tuple))

# # union
# x=frozenset(my_list)
# y=frozenset(my_list)
# print(x.union(y))

# import sys 

# my_list=[10,20,30,40,50]
# my_tuple=(10,20,30,40,50,60,70)
# my_set={10,20,30,40,50}

# lsize=sys.getsizeof(my_list)
# tsize=sys.getsizeof(my_tuple)
# ssize=sys.getsizeof(my_set)

# print(lsize)
# print(tsize)
# print(ssize)

import keyword

list=keyword.kwlist
print(list)