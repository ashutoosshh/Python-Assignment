from functools import reduce

def main():

    num=[1,2,3,4,5,6,7,8,9]


    max = reduce(lambda x, y: x if x>y else y ,num)


    print(max)


if __name__=="__main__":

    main()