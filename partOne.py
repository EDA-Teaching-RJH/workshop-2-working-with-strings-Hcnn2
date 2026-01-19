def main():
    slow = input("Where are you?")
    myFunction(slow)

def myFunction(text):
    fries = text.replace(' ','...')
    print(fries)

main()
