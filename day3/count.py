data = ''

with open('./day3/input.txt', 'r') as f:
    data = f.readlines()

def pad_data(data):
    res = []
    for datum in data:
        res.append('.'+datum+'.')
    return ['.'*len(res[0])] + res + ['.'*len(res[0])]

def group_numbers(string):
    #turns a string of the form ....123...3. into [[123, startindex, endindex],[3,...]]
    res = []
    i = 0
    while i < len(string):
        if 58>ord(string[i])>47:
            length = 0
            while 58>ord(string[i+length])>47:
                length +=1
            res.append([int(string[i:i+length]), i, i+length])
            i += length
        i+=1
    return res

def find_stars(string):
    #turns a string of the form .*.*..123...3. into [1,3]
    res = []
    for i, char in enumerate(string):
        if char =='*':
            res.append(i)
    return res

def char_in_string(string, chars):
    hit = False
    for char in chars:
        if char in string:
            hit = True
    return hit

def check_surroundings(cand, above, string, below):
    top = above[cand[1]-1:cand[2]+1]
    down = below[cand[1]-1:cand[2]+1]
    test_string = top+down+string[cand[1]-1:cand[2]+1]
    chars = ['+','@','/','$','&','*','-','#','%','=']
    return char_in_string(test_string, chars)

def surrounding_nums(cand, above, cand_row, below):
    res = 1
    found = 0
    for i in above+cand_row+below:
        if (cand+1>=i[1]>=cand-1) or (cand+1>=i[2]-1>=cand-1):
            found += 1
            res *= i[0]
    print(found)
    if found == 2:
        return res
    return 0

data1 = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''.split('\n')

padded_data = pad_data(data)
sum = 0

for i, datum in enumerate(padded_data):
    if i==0 or i==len(padded_data)-1:
        continue
    nums = group_numbers(datum)
    for num in nums:
        if check_surroundings(num, padded_data[i-1], datum, padded_data[i+1]):
            sum += num[0]

print(sum)

ratio = 0
tmp = []
for datum in padded_data:
    tmp.append(group_numbers(datum))

for i, datum in enumerate(padded_data):
    if i==0 or i==len(padded_data)-1:
        continue
    stars = find_stars(datum)
    for star in stars:
        print(i, star)
        ratio+=surrounding_nums(star, tmp[i-1], tmp[i], tmp[i+1])
print(ratio)