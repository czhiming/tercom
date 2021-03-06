#!/bin/sh

#使用初始设置，WMT17 sentence-level QE
######################################
ref_file=wmt17/train17.bpe.mt.output.postprocessed.dev
mt_file=wmt17/train17.tok.mt

hter_file=wmt17/train17.pred.hter
######################################


python make_trans.py $ref_file $mt_file
java -jar ../tercom.7.25.jar -r $ref_file.trans -h $mt_file.trans -o ter -n hter.output
python extract_hter.py hter.output.ter $hter_file

rm -f $ref_file.trans $mt_file.trans
rm -f hter.output.ter




