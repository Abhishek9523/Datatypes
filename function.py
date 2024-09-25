def add(x,y):
    return x+y,x-y,x*y,x/y,x%y,x//y
p=int(input("enter first number:"))
q=int(input("enter second number:"))
a,b,c,d,e,f=add(p,q)
print(a,b,c,d,e,f)