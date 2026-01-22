def main():


    no1=int(input("enter no1"))

    no2=int(input("enter no2"))

    no3=int(input("enter no3"))


    grater =lambda no1,no2,no3 :no1 if (no1>no2 and no1>no3 )else (no2 if no2 >no1  else( no3))



    print(grater(no1,no2,no3))



if __name__=="__main__":
    main()