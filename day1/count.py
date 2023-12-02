data = ''

with open('./day1/input.txt', 'r') as f:
    data = f.readlines()

def forward_sub_string(string):
    res = string
    for j in range(len(string)+1):
        for i, s in enumerate(nums):
            res = res[:j].replace(s, f'{i+1}') + res[j:]
    return res

def backward_sub_string(string):
    res = string
    for j in range(len(string)+1, -1, -1):
        for i, s in enumerate(nums):
            first_part = res[:j]
            last_part = res[j:].replace(s, f'{i+1}')
            res = res[:j] + res[j:].replace(s, f'{i+1}')
    return res

data1 = '''two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen'''.split('\n')
nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
sum = 0
list_a = []
for stringo in data:
    string = stringo
    forward = forward_sub_string(string)
    backward = backward_sub_string(string)
    first = 0
    last = 0
    first_index = 0
    last_index = 0
    for i, char in enumerate(forward):
        if 58>ord(char)>47:
            first = int(char)
            first_index = i
            break
    for i, char in enumerate(reversed(backward)):
        if 58>ord(char)>47:
            last = int(char)
            last_index = i
            break
    sum += 10*first + last
    list_a.append(10*first+last)
    #if forward != backward:
    #    print(f"{forward}, {backward}, {string}, {first}, {last}")
list_b = []
sum2 = 0
for string in data:
    first = first_i = last = last_i = 0
    for i, char in enumerate(string):
        if 58>ord(char)>47:
            first = int(char)
            first_i = i
            break

    for i, char in enumerate(reversed(string)):
        if 58>ord(char)>47:
            last = int(char)
            last_i = len(string)-i-1
            break

    for i, num in enumerate(nums):
        a = string.find(num)
        b = string.rfind(num)
        if -1 < a < first_i:
            first = i+1
            first_i = a
        if b > last_i:
            last = i+1
            last_i = b
    sum2 += first*10 + last
    list_b.append(first*10+last)
print(sum)
print(sum2)