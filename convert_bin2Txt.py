import sys

STOP_AT = 0x4ff
with open(sys.argv[1], 'rb') as f:
    hexList = ['0x{:02x}'.format(x) for x in f.read()][:STOP_AT]
    newList = [",".join(hexList[c:c+10]) for c in range(0, len(hexList), 10)]
    with open(sys.argv[2], 'w') as o:
        o.write("\n".join(newList))