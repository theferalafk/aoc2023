data = ''

with open('./day4/input.txt', 'r') as f:
    data = f.readlines()


data1 = '''Card   1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card   2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card   3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card   4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card   5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card   6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''.split('\n')

cards = [1 for i in range(len(data))]

sum = 0

for card_i, datum in enumerate(data):
    tmp = datum[10:].split('|')
    winning = tmp[0].split(' ')[:-1]
    drawn = tmp[1].split(' ')
    win_nums = []
    drawn_nums = []
    for i in winning:
        if i != '':
            win_nums.append(int(i))
    for i in drawn:
        if i != '':
            drawn_nums.append(int(i))
    hits = 0
    for i in drawn_nums:
        if i in win_nums:
            hits += 1
    for i in range(hits):
        if card_i+i >= len(data):
            break
        cards[card_i+i+1] += cards[card_i]
print(cards)
for i in cards:
    sum += i
print(sum)