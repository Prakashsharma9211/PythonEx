'''
x = int(input("Enter Number1 :")) 
y = int(input("Enter Number2 :")) 

if x>y :
	print("print ",x, "is greater then ",y) 
elif x<y :
	print("print ",x, "is smaller then ",y) 
else :
	print("print ",x, "is equal to ",x) 

'''


'''
while True:
	a = int(input("\nEnter Number1 :"))
	b = int(input("Enter Number2 :"))
	print(format(a, "b"))
	print(format(b, "b"))

	print("Bitwise &(AND) :", a&b,format(a&b, "b"))
	print("Bitwise |(OR) :", a|b,format(a|b, "b"))
	print("Bitwise ~(NOT) :", ~a,format(~a, "b"))

	print("Bitwise ^(XOR) :", a^b,format(a^b, "b"))
	print("Bitwise >>(R-Shift) :", a>>2,format(a>>2, "b"))
	print("Bitwise <<(L-Shift) :", a<<2,format(a<<2, "b"))

'''

Num = int(input(" Enter the Range of Number: ")) ; 
i = 0 ; 
first = 0; 
second = 1; 
while(i < Num): 
     if(i <= 1): 
        next = i ; 
     else: 
        next = first + second; 
        first = Ssecond; 
        second = next; 
        print(next);
        i = i + 1;




            