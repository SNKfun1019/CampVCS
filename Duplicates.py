#list = [a, b, b, b]
#count = 3
#remove = b
#count = 2
#remove = b
#count = 1
#while loop used --> while lst count("b") > 1 --> lst.remove("b")
#stop at one "b"
#print(my new list)
# aabbb --> for loop used

list = ["a", "a", "b", "b"]

while True:
    if list.count("a")=1:
        list.remove("a")
    elif list.count("b")=1:
        list.remove("b")
    else:
        break

print(list)