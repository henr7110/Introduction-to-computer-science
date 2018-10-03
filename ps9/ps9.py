# 6.00 Problem Set 9
#
# Name:
# Collaborators:
# Time:

from string import *

class Shape(object):
    def area(self):
        raise AttributeException("Subclasses should override this method.")

class Square(Shape):
    def __init__(self, h):
        """
        h: length of side of the square
        """
        self.side = float(h)
    def area(self):
        """
        Returns area of the square
        """
        return self.side**2
    def __str__(self):
        return 'Square with side ' + str(self.side)
    def __eq__(self, other):
        """
        Two squares are equal if they have the same dimension.
        other: object to check for equality
        """
        return type(other) == Square and self.side == other.side

class Circle(Shape):
    def __init__(self, radius):
        """
        radius: radius of the circle
        """
        self.radius = float(radius)
    def area(self):
        """
        Returns approximate area of the circle
        """
        return 3.14159*(self.radius**2)
    def __str__(self):
        return 'Circle with radius ' + str(self.radius)
    def __eq__(self, other):
        """
        Two circles are equal if they have the same radius.
        other: object to check for equality
        """
        return type(other) == Circle and self.radius == other.radius

#
# Problem 1: Create the Triangle class
#
## TO DO: Implement the `Triangle` class, which also extends `Shape`.
class Triangle(Shape):
    def __init__(self,base,height):
        '''
        Base: Base of the triangle
        Height: Height of the triangle
        '''
        self.base = float(base)
        self.height = float(height)
    def area(self):
        '''
        Returns the area of triangle

        '''
        return 0.5*self.base*self.height
    def __str__(self):
        '''
        Prints the base and height of the triangle
        '''
        return 'Triangle with base ' + str(self.base) + ' and height ' + str(self.height) 
    def __eq__(self, other):
        '''
        two triangles are the same if they have the same height and base
        '''
        return type(self) == Triangle and self.height == other.height and self.base == other.base
#
# Problem 2: Create the ShapeSet class
#
## TO DO: Fill in the following code skeleton according to the
##    specifications.

class ShapeSet:
    def __init__(self):
        """
        Initialize any needed variables
        """
        self.Shapes = []
        
    def __iter__(self):
        """
        Return an iterator that allows you to iterate over the set of
        shapes, one shape at a time
        """
        self.place = 0
        return self
    def next(self):
        if self.place >= len(self.Shapes):
            raise StopIteration
        self.place += 1
        return self.Shapes[self.place-1]
    def addShape(self, sh):
        """
        Add shape sh to the set; no two shapes in the set may be
        identical
        sh: shape to be added
        """
        #checks if the shapes are the same
        for i in self:
            if type(i) == type(sh) and i.area() == sh.area():
                raise ValueError("can't be same shape as is in set")
        #appends to set and increments length
        self.Shapes.append(sh)
    def __str__(self):
        """
        Return the string representation for a set, which consists of
        the string representation of each shape, categorized by type
        (circles, then squares, then triangles)
        """
        printer = ''
        for i in self:
            if type(i) == Circle:
                printer += str(i) + '\n'               
        for i in self:
            if type(i) == Triangle:
               printer += str(i) + '\n'
        for i in self:
            if type(i) == Square:
               printer += str(i) + '\n'
        printer = printer[:-1]
                
        return printer
        
#
# Problem 3: Find the largest shapes in a ShapeSet
#
def findLargest(shapes):
    """
    Returns a tuple containing the elements of ShapeSet with the
       largest area.
    shapes: ShapeSet
    """
    Areas = []
    Best = ()
    #generates list of areas
    for i in shapes:
        Areas.append(i.area())
    #finds max area
    Max = max(Areas)
    #adds the shapes with max area to Best
    for i in shapes:
        if i.area() == Max:
            Best += (i,)
    #returns Best
    return Best
        
def fl():
    c = Circle(5)
    e = Triangle(100,8)
    s = Square(10)
    b = Square(20)
    T = Triangle (1,3)
    d = Triangle (2,4)
    Set = ShapeSet()
    Set.addShape(c)
    Set.addShape(s)
    Set.addShape(b)
    Set.addShape(T)
    Set.addShape(d)
    Set.addShape(e)

    for i in findLargest(Set):
        print i
#
# Problem 4: Read shapes from a file into a ShapeSet
#
def readShapesFromFile(filename):
    """
    Retrieves shape information from the given file.
    Creates and returns a ShapeSet with the shapes found.
    filename: string
    """
    inputFile = open(filename)
    Set = ShapeSet()
    counter = 0
    #itterates through every line and adds the Shape to Set
    for line in inputFile:
        s = line.split(',')
        if len(s) == 3: #adds Triangle if lenght is 3
            s[2].strip('\n')
            Set.addShape(Triangle(s[1],s[2]))
        elif len(s) == 2: #adds either circle or square if lenght is 2
            s[1].strip('\n')
            if s[0] == 'square':
                Set.addShape(Square(s[1]))
            if s[0] == 'circle':
                Set.addShape(Circle(s[1]))
        else:
            print 'error', line
            raise ValueError('Shape not of known type')
    return Set
            

