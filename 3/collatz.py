def collatz(number):
    return 3 * number + 1 if number % 2 else number // 2


number = int(input("Number = "))
while number != 1:
    number = collatz(number)
    print(number)
