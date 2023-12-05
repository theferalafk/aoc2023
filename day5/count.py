data = ''

with open('./day5/input.txt', 'r') as f:
    data = f.read()

data1 = '''seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4'''

def split_numbers(data):
    res = []
    for datum in data:
        tmp = []
        for i in datum.split(' '):
            tmp.append(int(i))
        res.append(tmp)
    return res

def parse_data(data):
    #returns a very big array of the mapping:   [[seeds],[[mapping0_0],[mapping0_1]],[[mapping1_0],[mapping1_1]]]
    mappings = data.split(' map:')
    parsed_seeds = [int(i) for i in mappings[0].split('\n')[0].split(' ')[1:]]
    last = split_numbers(mappings[-1].split('\n')[1:])
    res = [parsed_seeds]
    for i in mappings[1:-1]:
        res.append(split_numbers(i.split('\n')[1:-2]))
    return res + [last]

def perform_mapping(num, mapping):
    res = num
    for i in mapping:
        if i[0]<=num<=i[0]+i[2]-1:
            offset = i[1] - i[0]
            res = num+offset
            break
    return res

parsed_data = parse_data(data)
mappings = parsed_data[1:]
mappings.reverse()
searching = True
num = 0
while searching:
    starting_value = num
    for maps in mappings:
        starting_value = perform_mapping(starting_value, maps)
    for i in range(0,len(parsed_data[0]),2):
        if parsed_data[0][i]<=starting_value<=parsed_data[0][i]+parsed_data[0][i+1]:
            print(starting_value)
            searching = False
    if num % 100000==0:
        print(num, starting_value)
    num += 1