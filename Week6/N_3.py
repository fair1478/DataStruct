def gcd(n1,n2):

    if n1<0:n1 *= -1
    if n2<0:n2 *= -1
    
    if n2 == 0:
        return n1
    elif n1==0 and n2 ==0:
        return -1
    x = n1 % n2
    if x==0:
        return n2
    else:
        return gcd(n2,x)
       
n1,n2 = map(int,input("Enter Input : ").split()) 
max = max(n1,n2)
min = min(n1,n2)
n1 = max
n2 = min
if(n1!=0 or n2!=0):
    print(f"The gcd of {n1} and {n2} is : {gcd(n1,n2)}")
else:
    print("Error! must be not all zero.")
    