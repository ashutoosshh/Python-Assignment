def main():

    print("Enter  value 1")
    value1=int(input())

    print("Enter Value 2")

    value2=int(input())

    print("min value is")
    min = lambda value1,value2 : value1 if value1<value2 else value2

    print(min(value1,value2))



if __name__=="__main__":

    main()