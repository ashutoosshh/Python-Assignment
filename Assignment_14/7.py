def main():
    print("Enter no")

    no =int(input())


    dev =lambda no : True if no%5==0 else False

    print(dev(no))



if __name__=="__main__":

    main()

    