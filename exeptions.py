# sys use to end the program at some points or lines
import sys
try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
     print("Erorr:  Invalid input")
     sys.exit(1)


try:
    results = x / y
except ZeroDivisionError:
    print("Erorr: Cannot divide by 0")
    sys.exit(1)
    # sys.exit(1) means if something wrong end the program without any extra messages.



print(f"{x} / {y} = {results}")