import threading

def Even():

    print("Even Thread Started")
    no = 2

    for i in range(10):
        print("Even:", no)
        no = no + 2


def Odd():

    print("Odd Thread Started")
    no = 1

    for i in range(10):
        print("Odd:", no)
        no = no + 2


def main():

    t1 = threading.Thread(target=Even)
    t2 = threading.Thread(target=Odd)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()
