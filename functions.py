def hello():
    name = input("Name: ")
    print("Hello " + name)
hello()

#() = argument

a = int(input("A: "))
b = int(input("B: "))

def sum(a,b):
    return a+b

#print or return

c = sum(a,b)
d = 2

e = sum(c,d) 
print(e)

# def duplicates(a,b,c,d):
#     list = [a,b,c,d]
#     for i in list:
#         while list.count(i)>1:
#             list.remove(i)
#         return list

# def calc(a,b):
#     sum = a+b
#     sub = a-b
#     mult = a*b
#     div = a/b
#     return sum,sub,mult,div

# print(calc(3,5))

#if calc(3,5) is = x, print(x)

# def list (*args):
#     for i in args:
#         print(i)
# list(10,20)

# def bye(name,age=125):
#     print("bye" + name)
#     print(str(age) + " years old")
# bye(name = " Ethan", age = 2)

# def outer_fun(a,b):
#     square = a ** 2
#     def addition(a,b):
#         return a+b
#     add = addition(a,b)
#     return add + square 
# print(outer_fun(4,6))

def outer_function(a,b):
    cubed = a ** 3
    def multiplication(a,b):
        return a*b
    multi = multiplication(a,b)
    def subtraction(a,b):
        return a-b
    subtract = subtraction(a,b)
    return subtract + multi + cubed
print(outer_function(5,4))
print("Yay!")
print("Bye~~~")
