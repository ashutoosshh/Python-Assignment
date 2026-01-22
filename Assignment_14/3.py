def main():


    value1=int(input())

    value2=int(input())


    max = lambda value1 , value2 : value1 if value1>value2 else value2


    print(max(value1,value2))



if __name__=="__main__":
    main()
    