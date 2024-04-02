import math

def area_of_rectangle():
    slength = input("Enter the length of your rectangle:")
    swidth = input("Enter the width of your rectangle:")
    l = float(slength) # convert string to float
    w = float(swidth) # convert string to float
    area = l * w
    return area

def area_of_triangle():
    sheight = input("Enter the height of your triangle:")
    sbase = input("Enter the base of your triangle:")
    h = float(sheight) # convert string to float
    b = float(sbase) # convert string to float
    area = 0.5 * b * h
    return area


def area_of_parallelogram():
    height = input("Enter the height of the parallelogram")
    breadth = input("Enter the breadth of the parallelogram")
    h = float(height)
    b = float(breadth)
    area = h * b
    return area


def area_of_square():
    side_input = input("Enter the side of a square:")
    side = int(side_input) # convert string to int
    area = side * side
    print("The area of the square is ", area)
    return area



def area_of_circle():
    r = float(input("Enter the radius of the circle"))
    area = math.pi * r * r
    return area


def area_of_trapezoid():
    h = float(input("Enter the height of the trapeziod"))
    ub = float(input("Enter the upper breadth of the trapeziod"))
    lb = float(input("Enter the lower breadth of the trapeziod"))
    
    area = 0.5 * h * (ub + lb)
    return area


if __name__ == '__main__':
    print("""
        RECTANGLE = 0
        TRIANGLE = 1
        CIRCLE = 2
        SQUARE = 3
        TRAPEZIOD = 4
        PARRALLELOGRAM = 5
        """)
    choice = int(input("What area do you want to calculate: "))
    area = None
    if choice == 0:
        area = area_of_rectangle()
    elif choice == 1:
        area = area_of_triangle()
    elif choice == 2:
        area = area_of_circle()
    elif choice == 3:
        area = area_of_square()
    elif choice == 4:
        area = area_of_trapezoid()
    elif choice == 5:
        area = area_of_parallelogram()
    else:
        print("What in the world did you choose. No calculation will be performed")
        area = "Nothing"
    
    print("The area calculated is ", area)