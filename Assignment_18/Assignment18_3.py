def main():
    print("Enter no of element want in insert")


    no =int(input())


    max=0
    
    empt=[]

    for i in range(no+1):
        print("enter no")

        it=int(input())

        empt.append(it)


    print(empt)


    for i in empt:
        if(i > max):
            max=i

        

        


    print("MAXIMUM NO IN LIST IS:")
    print(max)

        



    


if __name__=="__main__":

    main()