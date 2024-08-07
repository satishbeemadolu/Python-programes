"""8.	Print the average of three numbers entered
by the user by creating a class named 'Average'
having a function to calculate and print the
average without creating any object of the Average class"""

class Average:
    
    def calculate(a,b,c):
        return((a+b+c)/2)
    
x=int(input("enter first number: "))
y=int(input("enter second number: "))
z=int(input("enter third number: "))
print("Average : ",Average.calculate(x,y,z))
        
    
