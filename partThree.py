def main():
    pounds = pounds_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to charge? "))
    charge = pounds * percent
    print(f"Charge £{charge:.2f}")


def pounds_to_float(d):
    poundfloat = (d.slice(1,1))
    cf = float(poundfloat)


def percent_to_float(p):
    percentfloat = (p.slice(-1,-1))
    pf = float(percentfloat) / 100


main()
