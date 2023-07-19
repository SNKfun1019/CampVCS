# get the height from the user
# make height into an integer

# for i in range(height): (Important)
# print("#")
# h-1 = the space
# h+1 in the range

h = int(input("Height: "))

for i in range(1,h+1):
    print(" " * (h-i) + "#" * i)