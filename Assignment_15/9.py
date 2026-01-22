from functools import reduce



def main():


    num =[1,2,3,4,5,6,7,8,9]


    multi=reduce(lambda x,y :x*y,num)


    print(multi)


if __name__=="__main__":


    main()