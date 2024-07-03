# decorator is a function takes a function as input and return a modifi version as output

def announce(f):
    def wrapper():
        print("About to run the function..")
        f()
        print("Done with the function.")
    return wrapper

# @announce it means add the announce function to Hello function
@announce
def hello():
    print("Hello, World!")

hello()