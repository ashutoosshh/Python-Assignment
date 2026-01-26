def main():

    no=int(input())


    for i in range(0,no,1):
        for j in range(no-i):
            print("*",end="")

        print()


if __name__=="__main__":
    main()