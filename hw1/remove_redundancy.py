import sys
import re

infile = open(sys.argv[1], 'r')
output = [infile.readline()]
for line in infile:
    oline = line.split('\t')[0]
    for seg in line.split('\t')[1:]:
        oline = oline + '\t' + re.sub(r'(.)\1+', r'\1', seg)
    output.append(oline)
infile.close()

outfile = open(sys.argv[2], 'w')
for line in output:
    outfile.write(line)
outfile.close()
