def mul(no1,no2):

    print("multiplication is:",no1*no2)


def div(no1,no2):
    print("division is:",no1/no2)


def sub(no1,no2):
    print("substraction is:",no1-no2)

def add(no1,no2):
    print("addition is:",no1+no2)


def main():

    no1=int(input())
    no2=int(input())

    add(no1,no2)
    sub(no1,no2)
    div(no1,no2)
    mul(no1,no2)


if __name__=="__main__":
    main()