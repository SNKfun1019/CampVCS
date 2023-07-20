greeting = input("Greeting: ")

def bank(string):
    if greeting == "hello":
        print("$0")
    if greeting[0:] == "h":
        print("$20")
    else:
        print("$100")
print(bank)