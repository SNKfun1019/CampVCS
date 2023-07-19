food = ("pizza", "chicken", "malatang", "water", "pasta")
for x in food:
    if x == "malatang":
        break
    print(x)

drink = "coca cola"
for i in drink:
    print(i)

for i in range(5):
    print(i)

for j in range(10, 20):
    print(j)

for i in range(6):
    for j in range(2):
        print(i, j)

print("*")
print("*")
print("*")
print("*")
print("*")

for i in range(5):
    print("*")

print("*\n" * 5)

x = 1
for i in range(1,3):
    print("*" * i)
    print(x * i)

x = 0
while True:
    print("true")
    x = x + 1
    if x == 10:
        break
