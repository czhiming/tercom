#coding:utf8

import sys

ref_file = sys.argv[1]
hyp_file = sys.argv[2]

with open(ref_file+'.trans','w') as fp:
    for i,lines in enumerate(open(ref_file)):
        lines = lines.strip()
        lines += ' (sentence %d)' %  (i+1)
        fp.writelines(lines+'\n')
        
with open(hyp_file+'.trans','w') as fp:
    for i,lines in enumerate(open(hyp_file)):
        lines = lines.strip()
        lines += ' (sentence %d)' %  (i+1)
        fp.writelines(lines+'\n')







