class TorKham:
    def __init__(self):
        self.words = []
    def restart(self):
        self.words.clear()
        return "game restarted"
    def play(self, word):
        if not self.words:
            self.words.append(word)
            return self.words
        else:
            temp = self.words[len(self.words)-1].lower()
            ##print()
            if (temp[len(temp)-1] == word[1].lower()) and (temp[len(temp)-2] == word[0].lower()):
                self.words.append(word)
                return self.words
            else:
                return "game over"


torkham = TorKham()
word = []
print("*** TorKham HanSaa ***")

S = input("Enter Input : ").split(',')
for ele in S :
    if ele[0] == 'P' :
        temp = (ele).split(" ")
        print("'" + temp[1] + "'" + " -> ",end="")
        print(torkham.play(temp[1]))
    elif ele[0] == 'R' :
        print(torkham.restart())
    elif ele[0] == 'X' :
        break
    else:
        print("'" + ele + "'" + " is Invalid Input !!!")
        break