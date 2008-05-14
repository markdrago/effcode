#!/usr/bin/env python

import string, sys

trans = (3,13,20,4,8,12,24,5,18,19,6,23,9,17,7,16,10,1,15,14,11,26,2,21,25,22)

class EffCode:
    def __init__(self):
        keys = ''.join([chr(x + ord('A') - 1) for x in trans])
        vals = ''.join([chr(x) for x in range(ord('A'), ord('Z') + 1)])
        self.dec_table = string.maketrans(keys, vals)
        self.enc_table = string.maketrans(vals, keys)

    def decode(self, cypher):
        cypher = cypher.upper()
        clears = []
        for chunk in cypher.split('  '):
            interm = self.create_alpha_decode_str(chunk)
            clears.append(interm.translate(self.dec_table))
        return ' '.join(clears)

    def encode(self, clear):
        clear = clear.upper()
        cyphers = []
        for chunk in clear.split(' '):
            interm = chunk.translate(self.enc_table)
            cyphers.append(self.create_alpha_encode_str(interm))
        return '  '.join(cyphers)

    def create_alpha_decode_str(self, cypher):
        return ''.join([chr(int(x) + ord('A') - 1) for x in cypher.split(' ')])

    def create_alpha_encode_str(self, clear):
        return ' '.join([str(ord(x) - ord('A') + 1) for x in clear])

def usage():
    print "Usage: -d <cypher>, -e <clear>"
    sys.exit(1)

if __name__ == '__main__':
    effcode = EffCode()
    if len(sys.argv) != 3:
        usage()
        
    if sys.argv[1] == '-d':
        print effcode.decode(sys.argv[2])
    elif sys.argv[1] == '-e':
        print effcode.encode(sys.argv[2])
    else:
        usage()

    sys.exit(0)
