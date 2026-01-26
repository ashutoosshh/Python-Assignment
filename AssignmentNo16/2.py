def chckname(no):

    if(no%2==0):
        print("no is even")

    else:
        print("no is odd")


def main():

    print ("Enter NO")
    chckname(int(input()))

if __name__=="__main__":

    main()


