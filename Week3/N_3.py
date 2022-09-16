class Stack:

    def __init__(self):
        self.stk = []
    def push(self, value):
        self.stk.append(value)
    def pop(self):
        return self.stk.pop()
    def size(self):
        return str(len(self.stk))
    def peek(self):
        return self.stk[-1]
    def isEmpty(self):
        if len(self.stk) == 0:
            return True
        elif len(self.stk) >0:
            return False

inp = input('Enter Infix : ')

S = Stack()

print('Postfix : ', end='')

operator = ["+","-","*","/"]
operator_more = ["+","-","*","/","(",")","^"]
dict_operator = { '+':2 , '-':2 , '*':3 , '/':3 ,'^':4}
kumtob = ""
for item in inp:
    if item not in operator_more:
        kumtob += item  #push ตัวอักษร
    else:
        if item == "(":
            S.push(item)
        elif item == ")":
            while not S.peek() == "(":
                kumtob += S.peek()
                S.pop()
            S.pop()
        else:
            if not S.isEmpty():
                
                if S.peek() != "(":
                    # print(dict_operator.get(item) <= dict_operator.get(S.peek()))
                    if dict_operator.get(item) <= dict_operator.get(S.peek()) :
                        kumtob += S.peek()
                        S.pop()
                        while not S.isEmpty() and S.peek() != "(" and dict_operator.get(item) <= dict_operator.get(S.peek()) :
                            kumtob += S.peek()
                            S.pop()
                        S.push(item)
                    else:
                        S.push(item)
                else:
                    S.push(item)
            else:
                S.push(item)
print(kumtob,end='')
while not S.isEmpty():

    print(S.peek(), end='')
    S.pop()

print()