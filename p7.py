"""7.	Write a program to print the area of a rectangle
by creating a class named 'Area' taking the values of its
length and breadth as parameters of its constructor and
having a function named 'returnArea' which returns the
area of the rectangle. Length and breadth of the rectangle
are entered through keyboard."""

class Area:
    def __init__(self,length,breadth):
        self.l=length
        self.b=breadth
    def returnArea(self):
        area=(self.l*self.b)
        return area 

print("Enter the length of the rectangle: ")
a=int(input())
print("enter the breadth of the rectangle: ")
b=int(input())
obj=Area(a,b)
print("Area of the rectangle: ",obj.returnArea())
                
