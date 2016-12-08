import sys
import struct

def swap_and_decode(i):
    return format(struct.unpack("<I", struct.pack(">I", i))[0], '04x').decode('hex')

hex_input = sys.argv[1]
n = 8

strings = list()

for hex_value in [hex_input[i:i+n] for i in range(0, len(hex_input), n)]:
    int_str = int(hex_value, 16)
    strings.append(swap_and_decode(int_str))

print ''.join(strings)
