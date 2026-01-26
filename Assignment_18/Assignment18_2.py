def main():
    

    no=int(input("Enter length of list"))
    lis=[]

    count=0


    for i in range(no+1):

        tt=int(input("enter element"))

        lis.append(tt)

    print(lis)

    no1=int(input("Enter the no which you want to check ferquency"))

    for i in lis:
        if (no1==i):
            count=count+1

    print(count)


if __name__=="__main__":

    main()