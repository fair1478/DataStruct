class funString():

    def __init__(self,inString):

        self.inString = inString

    def __str__(self):

        return self.inString

    def size(self) :

        return str(len(self.inString))

    def changeSize(self):
        return str(self.inString.swapcase())

    def reverse(self):
        temp = str("")
        for x in range(len(self.inString)-1,-1,-1):
            temp += self.inString[x]
        self.inString = temp
        return str(self.inString)

    def deleteSame(self):
        temp = str("")
        for x in self.inString:
            if x not in temp:
                temp += x
        return temp

str1,str2 = input("Enter String and Number of Function : ").split()

res = funString(str1)

if str2 == "1" :    print(res.size())

elif str2 == "2":  print(res.changeSize())

elif str2 == "3" : print(res.reverse())

elif str2 == "4" : print(res.deleteSame())