def main():


    num=[1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20]



    odd =list(filter(lambda x : x % 2 !=0 ,num))


    print(odd)



if __name__=="__main__":
    main()