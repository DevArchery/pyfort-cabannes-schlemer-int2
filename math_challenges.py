import math
import random as rnd
def factorial(n):
    """Calculate the factorial of n"""
    try:
        assert n>=0, "n must be a positive integer"

        if n==0:
            return 1
        else:
            return n*factorial(n-1)
    except AssertionError:
        return ValueError
def factorial_challenge(n=None)->bool:
    """Implement a challenge where the player has to calculate the factorial of a random number"""
    try:
        if n is None:
            n=rnd.randint(1,10)
        print(f"Calculate the factorial of {n}")
        guess=int(input())
        fac=factorial(n)
        if guess==fac:
            print("Congratulations! You found the factorial!")
            return True
        else:
            print("You lost! The factorial of", n, "is", fac)
            return False
    except TypeError:
        return ValueError
    except ValueError:
        print("Please enter an integer")
        return factorial_challenge()


def linear_equation():
    a,b=rnd.randint(1,10), rnd.randint(-10,10)
    sol=-b/a
    return a,b,sol

def math_challenge_equation(a=None,b=None,sol=None)->int:
    """Implement a challenge where the player has to solve a linear equation"""
    try:
        if a is None and b is None and sol is None:
            a,b,sol=linear_equation()
            assert len(str(sol))<=5

        if b<0:
            print(f"Solve the equation {a}x - {-b} = 0")
        elif b==0:
            print(f"Solve the equation {a}x = 0")
        else:
            print(f"Solve the equation {a}x + {b} = 0")
        guess=float(input())
        if guess==sol:
            print("Congratulations! You found the solution!")
            return True
        else:
            print("You lost! The solution is", -b/a)
            return False
    except ZeroDivisionError:
        return ValueError
    except ValueError:
        print("Please enter a floating point number")
        return math_challenge_equation(a,b,sol)
    except AssertionError:
        return math_challenge_equation()
def is_prime(n):
    """Check if n is a prime number"""
    try:
        assert n>=2, "n must be greater than 1"
        for i in range(2, int(math.sqrt(n))+1):
            if n%i==0:
                return False
        return True
    except AssertionError:
        return ValueError
def nearest_prime(n)->int:
    if is_prime(n):
        return n
    else:
        for i in range(n+1,21):
            if is_prime(i):
                return i
    return 23
def math_challenge_prime()->bool:
    """Implement a challenge where the player has to find the nearest prime number to a random number"""
    n=rnd.randint(1,20)
    print(f"Find the nearest prime number to {n}")
    guess=int(input())
    prime=nearest_prime(n)
    if guess==prime:
        print("Congratulations! You found the prime number!")
        return True
    else:
        print("You lost! The nearest prime number to", n, "is", prime)
        return False

def math_roulette():
    """Implement a challenge where the player has to guess the result of a mathematical operation"""
    numbers=[rnd.randint(1,10) for i in range(5)]
    op=rnd.choice(["+","-","*"])
    sol=numbers[0]
    if op=="+":
        for i in range(1,5):
            sol+=numbers[i]
    elif op=="-":
        for i in range(1,5):
            sol-=numbers[i]
    elif op=="*":
        for i in range(1,5):
            sol*=numbers[i]
    print(f"Calculate {numbers[0]} {op} {numbers[1]} {op} {numbers[2]} {op} {numbers[3]} {op} {numbers[4]} = ?")
    guess=float(input())
    if guess==sol:
        print("Congratulations! You found the result!")
        return True
    else:
        print("You lost! The result is", sol)
        return False


def math_challenges():
    challenges=[math_challenge_equation,factorial_challenge,math_challenge_prime,math_roulette]
    return rnd.choice(challenges)()

if __name__=="__main__":
    math_challenges()