def checkno(no):

    if(no==0):
        print("No is Zero")


    elif(no<0):
        print("NO is negative")

    else:
        print("No is positive")











def main():

    print("Enter no which you want check")
    checkno(int(input()))



if __name__=="__main__":
    main()