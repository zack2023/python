# oop
# __init__ will called automaticly everytime i call the point
# self is reprisint the object in questions

class point():
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2

# 2 is the value of x, 8 is the value of y
p = point(2, 8)
print(p.x)
print(p.y)
