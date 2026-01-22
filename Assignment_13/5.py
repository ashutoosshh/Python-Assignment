def main():

    print("Enter marks")
    no=int(input())



    if(no>75 and no<100):
        print("Distinction")


    elif(no>65 and no<75):
        print("A+ Grade")

    elif(no>50 and no<65):
        print("B grade")

    elif(no>35 and no<50):
        print("PASS")

    elif(no<35):
        print("FAIL")





if __name__=="__main__":
    main()