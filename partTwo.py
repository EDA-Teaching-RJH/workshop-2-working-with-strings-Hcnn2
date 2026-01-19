import math  

def main():
    A = float(input('A='))
    B = float(input('B='))
    pythag(A,B)

def pythag(A,B):
    A1 = A**2
    B1 = B**2
    C1 = A1 + B1
    C = int(C1**0.5)
    print(C)

main()
