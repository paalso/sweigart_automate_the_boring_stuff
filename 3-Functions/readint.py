def readint():
    while True:
        print("Input an integer: ")
        try:
            n = int(int(input()))
            return n
        except:
            print("It's not an integer. Try again.")


number = readint()
