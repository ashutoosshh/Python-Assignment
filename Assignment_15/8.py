def main():
    
    num=[3,5,15,30,40,45,50,60,75,56,90]



    fil=list(filter(lambda x:  x % 3 ==0 and x % 5 ==0 , num))


    print(fil)


if __name__=="__main__":
    main()
