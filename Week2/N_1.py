class Calculator :

    def __init__(self,n1):
        
        self.num1 = n1

    def __add__(self,n2):

        return self.num1 + n2

    def __sub__(self,n2):

        return self.num1 - n2


    def __mul__(self,n2):

        return self.num1 * n2

    def __truediv__(self,n2):

        return self.num1 / n2

x,y = input("Enter num1 num2 : ").split(",")

x,y = Calculator(int(x)),Calculator(int(y))

print(x.__add__(y.num1),x.__sub__(y.num1),x.__mul__(y.num1),x.__truediv__(y.num1),sep = "\n")