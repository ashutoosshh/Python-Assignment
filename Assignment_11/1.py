def main():

    no =int(input("enter no"))


    if (no<1):

        print("no is no t prime no")
        return

    is_prime =True
    


    for i in range(2,int(no**0.5)+1):

        if (no % i== 0):

            print("is not prime no")

            is_prime = False
            break


    if is_prime:
        print("is prime no")

    else:
        print("not a prime no")




if __name__=="__main__":

    main()
