# my_dict=dict()
# print(my_dict)
# print(type(my_dict))
# print(id(my_dict))

# my_dict['name']="abhishek"
# print(my_dict)
# print(id(my_dict))

# my_dict['qualification']="BCA"
# print(my_dict)

# my_dict['name']="Prince"
# print(my_dict)
# print(type(my_dict))
# print(id(my_dict))

# del my_dict['name']
# print(my_dict)

# my_dict.clear()
# print(my_dict)

# print(len(my_dict))
# print(max(my_dict))
# print(min(my_dict))

# my_dict.keys()
# print(my_dict.keys)

# my_dict.items()
# print(my_dict.items)

# my_dict.values()
# print(my_dict.values)

# print(my_dict.get('key','Guest'))

# my_dict.pop('name')
# print(my_dict)

# my_dict.popitem()
# print(my_dict)

# del my_dict
# print(my_dict)



# dict1={123 : ["ajay",961235489],
#        456 : ["vijay",9876545454],
#        789 : ["sagar", 5473585683]
#        }
# dict1[458]=["dinesh",62004587]
# dict1.update({567:["abhishek",9523770350]})
# print(dict1)

records={}

n=int(input("how many ?????")) 

for i in range(n):
       aadhar=int(input("enter aadhar:"))
       name=input("enter name:")
       mobile=input("enter mobile:")
       d={"mame":name,"mobile":mobile}
       records[aadhar]=d
print(records)       