"""Print the sum, difference and product of two complex numbers
by creating a class named 'Complex' with separate functions
for each operation whose real and imaginary parts are entered
by the user."""

class Complex:
    def sum(a,b):
        return(a+b)
    def difference(a,b):
        return(a-b)
    def product(a,b):
        return(a*b)
u=int(input("enter firest real number     : "))
v=int(input("enter first imaginary number : "))
l=complex(u,v)
print("First complex number : ",l)

w=int(input("enter second real number      : "))
x=int(input("enter second imaginary number : "))
m=complex(w,x)
print("Second complex number : ",m)
print()

print("sum of two complex numbers        : ",Complex.sum(l,m))
print("Difference of two complex numbers : ",Complex.difference(l,m))
print("Product of two complex numbers    : ",Complex.product(l,m))
