def main():

    print("Enter no")

    no=int(input())


    even =lambda no :True if no % 2 == 0 else False



    print(even(no))



if __name__=="__main__":
    main()