import sys

mapping = {
'00': '',
'04': 'a',
'05': 'b',
'07': 'd',
'06': 'c',
'08': 'e',
'09': 'f',
'0a': 'g',
'0b': 'h',
'0c': 'i',
'0d': 'j',
'0e': 'k',
'0f': 'l',
'10': 'm',
'11': 'n',
'12': 'o',
'13': 'p',
'14': 'q',
'15': 'r',
'16': 's',
'17': 't',
'18': 'u',
'19': 'v',
'1a': 'w',
'1b': 'x',
'1c': 'y',
'1d': 'z',
'1e': '1',
'1f': '2',
'20': '3',
'21': '4',
'22': '5',
'23': '6',
'24': '7',
'25': '8',
'26': '9',
'27': '0',
'28': '\n',
'37': '.',
'2d': '-',
'2f': '[',
'30': ']',
'34': '\'',
'4f': '>',
'50': '<',
}

maj_mapping = {
'00': '',
'1e': '!',
'1f': '@',
'20': '#',
'21': '$',
'22': '%',
'23': '^',
'24': '&',
'25': '*',
'26': '(',
'27': ')',
'2d': '_',
'2f': '{',
'30': '}',
}

with open(sys.argv[1], 'r') as f:
    data = f.read()

l = list()

for line in data.splitlines():
    if line.split(':')[0] == '02':
        if line.split(':')[2] in maj_mapping:
            l.append(maj_mapping[line.split(':')[2]])
        else:
            l.append(mapping[line.split(':')[2]].upper())
    else:
        l.append(mapping[line.split(':')[2]])

print ''.join(l)
