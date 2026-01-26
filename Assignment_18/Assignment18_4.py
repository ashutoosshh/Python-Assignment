def main():
    print("Enter no of element want in insert")


    no =int(input())


    min=100
    
    empt=[]

    for i in range(no):
        print("enter no")

        it=int(input())

        empt.append(it)


    print(empt)


    for i in empt:
        if(i < min):
            min=i

        

        


    print("MINIMUM NO IN LIST IS:")
    print(min)

        



    


if __name__=="__main__":

    main()