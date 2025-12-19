def square():
    l = int(input("Enter length of square:"))
    area = l * l
    perimeter = 4*l
    print(f"Area of square is: {area}")
    print(f"Perimeter of square is: {perimeter}")
    
def cube():
    l = int(input("Enter length of cube:"))
    volume = l * l * l
    print(f"Volume of cube is: {volume}")

def rectangle():
    l = int(input("Enter length of rectangle:"))
    b = int(input("Enter breadth of rectangle:"))
    area = l * b
    perimeter = 2 * (l + b)
    print(f"Area of rectangle is: {area}")
    print(f"Perimeter of rectangle is: {perimeter}")

def circle():
    r = int(input("Enter radius of circle:"))
    area = (22/7)*r
    perimeter = 2 * (22/7) * r
    print(f"Area of circle is: {area}")
    print(f"Perimeter of rectangle is: {perimeter}")

square()
rectangle()
circle()