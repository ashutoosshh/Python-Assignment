def main():
    print("Enter no")
    no=int(input())
    ttl=0

    for i in range(1,no+1):
        if(  no % i==0):
           
           ttl=ttl+i
        else:
            pass
    print(ttl)   
        

          


if __name__=="__main__":

    main()