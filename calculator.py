print("Welcome to Sophie's Calculator\n")

#create 2 variables (x and y)
x = int(input("What is your first number?"))
y = int(input("What is your second number?"))

#get add, subtract, multiply, or divide
math = input("What would you like to do with these number?\n")

if math == "add":
    print(x, "+", y, "=", x+y)

elif math == "substract":
    print(x, "-", y, "=", x-y)

elif math == "multiply":
    print(x, "x", y, "=", x*y)

elif math == "divide":
    print(x, "/", y, "=", x/y )