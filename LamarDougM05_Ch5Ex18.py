"""
Write program to determine prime number.

Example, 5 is a prime number, but 6 is not.

"""

def user_input():
    u_input = int(input("Please enter a number."))
    return u_input

def is_prime(x):
    if x <= 1:
        return False
    else:
        i = 2
        while x > i:
            if x % i == 0:
                return False
            else:
                i += 1

        else:
            return True

def number(boolean):
    print(boolean)


def all_prime():
    for num in range(1, 101):
        pri = is_prime(num)
        if pri == True:
            print(num)


def main():

    nums = user_input()

    boolean = is_prime(nums)

    number(boolean)

    all_prime()

    print("Doug Lamar")

main()


  

    
