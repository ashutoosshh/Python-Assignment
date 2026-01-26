def main():
    print("Enter no of element want in insert")


    no =int(input())


    sum=0
    empt=[]

    for i in range(no+1):
        print("enter no")

        it=int(input())

        empt.append(it)


    print(empt)


    for empt in range(len(empt)+1):

        sum=sum+empt


    print("Total addition of all element in list is:")
    print(sum)

        



    


if __name__=="__main__":

    main()