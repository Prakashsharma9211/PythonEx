'''
#fibnocchi in python

Num =int(input('Enter the range'))
i=0 
f=0 
s=1
print(f,",",s,end=",")
while i < Num:
    t=f+s
    f=s
    s=t
    print(t,end=",")
    i=i+1


    


#factorial in python

num=int(input("Enter number:"));
fact=1 ;
while(num>0):
     fact=fact*num;
     num=num-1 ;
print("Factorial of the number is: ") ;
print(fact);




#Palindrome of a number
n=int(input("Enter number:"))  
temp=n  
rev=0  
while(n>0): 
     dig=n%10
     rev = rev*10+dig 
     n=n //10; 

if(temp==rev): 
     print("The number is a palindrome") 
else: 
     print("The number is not a palindrome")



#Armstrong Number in Python
num = int(input("Enter a number: ")) 
sum = 0; 
temp = num ; 
while temp > 0:
     digit = temp % 10 
     sum += digit ** 3  
     temp //=12 10 ; 
if num == sum: 
     print(num,"is an Armstrong number")  
else: 
     print(num,"is not an Armstrong number")

'''
