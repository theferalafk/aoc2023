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

def range_to_mapping(mapping):
    res = {}
    for i in mapping:
        for j in range(i[2]):
            res[j+i[1]]=j+i[0]
    return res

def perform_mapping(num, mapping):
    res = num
    for i in mapping:
        if i[1]<=num<=i[1]+i[2]:
            offset = i[0]-i[1]
            res = num+offset
            break
    return res

parsed_data = parse_data(data)

array_mapping = []
for i in parsed_data[1:]:
    a=1#array_mapping.append(range_to_mapping(i))

res = []
print(parsed_data[0])
for i in range(0,len(parsed_data[0]),2):
    print(parsed_data[0][i])
    rangethings = [parsed_data[0][i]+j for j in range(parsed_data[0][i],parsed_data[0][i]+parsed_data[0][i+1])]
    #print(len(rangethings))
    print("starting...")
    for k in rangethings:
        tmp = k
        for mapping in parsed_data[1:]:
            tmp = perform_mapping(tmp, mapping)
        res.append(tmp)
print(min(res))