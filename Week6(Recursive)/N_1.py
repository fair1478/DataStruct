def Factorial(n):
    if n == 1 or n==0:
        return 1
    return Factorial(n-1) + n

inp = int(input("Enter Number : "))

print(f'{inp}! = {Factorial(inp)}')