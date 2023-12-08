from collections import Counter

data = ''

with open('./day7/input.txt', 'r') as f:
    data = f.read()

data1 = '''32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483'''
data2 ='''23456 1
23455 2
23344 3
23444 4
22333 5
23333 6
22222 7'''
data1 = '''34437 182
JJ293 449
J9999 607
JJQJA 446'''
def determine_class(hand):
    win_class = len(Counter(hand))
    true_class = 0
    if win_class == 1:
        true_class = 7
    elif win_class == 2:
        counts = list(Counter(hand).values())
        counts.sort()
        true_class = 7-counts[0]
    elif win_class == 3:
        counts = list(Counter(hand).values())
        counts.sort()
        true_class = 1+counts[2]
    else:
        true_class = 6-win_class
    return true_class

def calc_joker_score(hand):
    amount = hand.count('1')
    tmp = []
    for i, character in enumerate(hand):
        if character == '1':
            tmp.append(chr(0x41+i))
        else:
            tmp.append(character)
    true_class = determine_class(tmp)
    for i in range(amount):
        match true_class:
            case 7:
                pass
            case 6:
                true_class=7
            case 5 | 4:
                true_class=6
            case 3:
                true_class=5
            case 2:
                true_class=4
            case 1:
                true_class=2
    return true_class

def score_hand(hand):
    #takes [card0,...,card4] and calculates a score based on it
    #score is class of winning || card as hex value, where A is 14 and 2 is 2
    score = 0
    if '1' in hand:
        true_class = calc_joker_score(hand)
    else:
        true_class = determine_class(hand)
    score += (16**5)*true_class
    for i, card in enumerate(hand):
        score += (16**(4-i))*int(card,16)
    return score

def parse_data(data):
    #returs [Card0,...Card4, score, Bid]
    #class 0 is five of a kind, class 6 is high card
    clean = data.replace('T','a').replace('J','1').replace('Q','c').replace('K','d').replace('A','e')
    res = []
    for bet in clean.split('\n'):
        tmp = []
        split_str = bet.split(' ')
        for card in split_str[0]:
            tmp.append(card)
        tmp.append(score_hand(tmp))
        tmp.append(int(split_str[1]))
        res.append(tmp)
    res.sort(key=lambda x: x[5])
    return res



parsed_data = parse_data(data)


#765, 220, 28, 684, 483

sum = 0
res = []
for i, bet in enumerate(parsed_data):
    sum += bet[-1]*(i+1)
    res.append(bet[-1])
print(sum)