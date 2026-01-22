
from functools import reduce


def main():



    num=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]



    sum = reduce(lambda x,y:x+y ,num)



    print(sum)



if __name__=="__main__":

    main()