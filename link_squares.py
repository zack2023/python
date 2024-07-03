# here we will try to link this file with functions2.py file
# from functions import square is to import the function square here
# so we can use it in this file
#-------------------------------------------------
# another way is to write import functions
# but in the print line i have to add functions.(name of function)
# for example: print(f"The square of {i} is {functions.square(i)}")

from functions import square
for i in range(10):
    print(f"The square of {i} is {square(i)}")