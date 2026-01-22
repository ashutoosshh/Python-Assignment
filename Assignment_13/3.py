def main():

    print ("Enter no")

    no=int(input())
    sum=0
    lis=[]

    for i in range(1,no-1):

        if( no % i==0):
            lis.append(i)



    for value in lis:

        sum=sum +value


    if(sum==no):
        print("no is perfect")

    else:
        print("no is not perfect")




if __name__=="__main__":
    main()





