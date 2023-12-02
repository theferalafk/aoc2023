data = ''

with open('./day2/input.txt', 'r') as f:
    data = f.readlines()
#           r b g
config = [12, 13, 14]

def parse_game(game):
    #return an array where each entry is the number of colors per draw [r,g,b]
    res = []
    for round in game.split(';'):
        tmp = []
        r = round.find('red')
        g = round.find('green')
        b = round.find('blue')

        if r>-1:
            if 58>ord(round[r-3])>47:
                tmp.append(int(round[r-3])*10 + int(round[r-2]))
            elif 58>ord(round[r-2])>47:
                tmp.append(int(round[r-2]))
            else:
                tmp.append(0)
        else:
            tmp.append(0)

        if g>-1:
            if 58>ord(round[g-3])>47:
                tmp.append(int(round[g-3])*10 + int(round[g-2]))
            elif 58>ord(round[g-2])>47:
                tmp.append(int(round[g-2]))
            else:
                tmp.append(0)
        else:
            tmp.append(0)

        if b>-1:
            if 58>ord(round[b-3])>47:
                tmp.append(int(round[b-3])*10 + int(round[b-2]))
            elif 58>ord(round[b-2])>47:
                tmp.append(int(round[b-2]))
            else:
                tmp.append(0)
        else:
            tmp.append(0)
        res.append(tmp)
    return res

def get_max(game):
    res = [0,0,0]
    for i in range(3):
        for round in game:
            if round[i]>res[i]:
                res[i]=round[i]
    return res

data1 = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''.split("\n")

sum = 0
pow_sum = 0
for i, game in enumerate(data):
    parsed_game = parse_game(game)
    max_list = get_max(parsed_game)
    if (config[0]>=max_list[0]) and (config[1]>=max_list[1]) and (config[2]>=max_list[2]):
        sum += i+1
    pow_sum += max_list[0]*max_list[1]*max_list[2]
print("star 1:", sum)
print("star 2:", pow_sum)