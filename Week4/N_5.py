class Queue:

    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join(self.queue)

    def push(self, data):
        self.queue.append(data)

    def pop(self):
        return self.queue.pop(0) if self.size() != 0 else 'Empty'

    def size(self):
        return len(self.queue)

def display(red, heat, mistake, blue, freeze):
    print('NORMAL :')
    print(len(red))
    print(''.join(str(a) for a in reversed(red)) if len(red) != 0 else 'Empty')
    print(f'{heat} Explosive(s) ! ! ! (NORMAL)')
    if mistake != 0:
        print(f'Failed Interrupted {mistake} Bomb(s)')
    print('------------MIRROR------------')
    print(': RORRIM')
    print(len(blue))
    print(''.join(str(a) for a in reversed(blue)) if len(blue) != 0 else 'ytpmE')
    print(f'(RORRIM) ! ! ! (s)evisolpxE {freeze}')


if __name__ == '__main__':
    red, blue = input('Enter Input (Normal, Mirror) : ').split()
    red = list(red)
    blue = list(blue)

    bq, bomb_blue, freeze = Queue(), [], 0
    for i in range(-1, -len(blue) - 1, -1):
        bomb_blue.append(str(blue[i]))
        if len(bomb_blue) > 2:
            if bomb_blue[-1] == bomb_blue[-2] == bomb_blue[-3]:
                bq.push(str(blue[i]))
                freeze += 1
                for a in range(3):
                    bomb_blue.pop()

    bomb_red, heat, mistake = [], 0, 0
    for i, data in enumerate(red):
        bomb_red.append(data)
        if len(bomb_red) > 2:
            if bomb_red[-1] == bomb_red[-2] == bomb_red[-3]:
                bq_pop = bq.pop()
                if data == bq_pop:
                    for a in range(2):
                        bomb_red.pop()
                    mistake += 1
                elif bq_pop == 'Empty':
                    for a in range(3):
                        bomb_red.pop()
                    heat += 1
                else:
                    bomb_red.insert(-1, bq_pop)

    #print(''.join(str(a) for a in reversed(bomb_red)) if len(bomb_red) != 0 else 'Empty')
    display(bomb_red, heat, mistake, bomb_blue, freeze)