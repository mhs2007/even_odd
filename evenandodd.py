
import sys

def evenodd(n):
    if(n%2 == 0):
        return "Even Number"
    else:
        return "Odd Number"
if __name__ == "__main__":
    n = int(sys.argv[1])

    print("The Result is: ",evenodd(n))