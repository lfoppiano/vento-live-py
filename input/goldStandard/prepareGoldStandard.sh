#!/usr/bin/env bash

INPUT=$1
OUTPUT=$2
for x in $INPUT/1.0/*; do tr -d '\n' < $x >> $OUTPUT/tmp_1.0; echo "" >> $OUTPUT/tmp_1.0 ; done
sed -n 's:.*<text>\(.*\)</text>.*:\1:p' $OUTPUT/tmp_1.0 > $OUTPUT/1.0
sort --parallel=8 $OUTPUT/1.0 | uniq > $OUTPUT/1.0.csv
rm tmp_1.0
for x in $INPUT/2.0/*; do tr -d '\n' < $x >> $OUTPUT/tmp_2.0; echo "" >> $OUTPUT/tmp_2.0 ; done
sed -n 's:.*<text>\(.*\)</text>.*:\1:p' $OUTPUT/tmp_2.0 > $OUTPUT/2.0
sort --parallel=8 $OUTPUT/2.0 | uniq > $OUTPUT/2.0.csv
rm tmp_2.0
for x in $INPUT/3.0/*; do tr -d '\n' < $x >> $OUTPUT/tmp_3.0; echo "" >> $OUTPUT/tmp_3.0 ; done
sed -n 's:.*<text>\(.*\)</text>.*:\1:p' $OUTPUT/tmp_3.0 > $OUTPUT/3.0
sort --parallel=8 $OUTPUT/3.0 | uniq > $OUTPUT/3.0.csv
rm tmp_3.0