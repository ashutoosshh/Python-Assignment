def main():



    num =[1,2,3,4,5,6,7,8,9]

    

    coun=list(filter(lambda x:  x % 2==0 , num))


    count =len(coun)



    print("count of even num in list is",count)

    



if __name__=="__main__":

    main()