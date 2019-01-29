import math

a = int(input("Enter the value 1"))
b = int(input("Enter the value 2"))
c = int(input("Enter the value 3"))
d = (b*b) - (4*a*c)
if(d>0):
    print("Roots are Equal")
    sol1 = ((-b)+ math.sqrt(d))/(2*a)
    sol2 = ((-b)- math.sqrt(d))/(2*a)
elif(d<0) :
     print("Roots are complex")
     
else:
    print("Roots are Equal")
    
print('The solution are {0} and {1}'.format(sol1,sol2))


