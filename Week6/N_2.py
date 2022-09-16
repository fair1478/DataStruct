def length(txt):
    global s
    global i
    i+=1
    if txt != '':
        if i % 2 == 0:
            s += txt[0] + "*"
        else:
            s += txt[0] + "~"
    if txt == '':
        return 0
    else: return length(txt[1:])

i=-1
s=""
length(input("Enter Input : "))
print(s,i,sep="\n")
