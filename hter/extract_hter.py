#coding:utf8

import sys

hter_in = sys.argv[1]
hter_out = sys.argv[2]


with open(hter_out,'w') as fp:
    for i,lines in enumerate(open(hter_in)):
        if i == 0 or i == 1:
            pass
        else:
            lines = lines.strip().split()
            hter = lines[4]
            fp.writelines(hter+'\n')
            
        









