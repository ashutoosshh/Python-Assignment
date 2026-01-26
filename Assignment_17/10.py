def main():


    no=int(input())

    add=0
    

    while(no>0):

       

        gun =no %10

        add =add+gun
        no =no //10

    print(add)



if __name__=="__main__":

    main()
