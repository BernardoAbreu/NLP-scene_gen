#!/bin/bash

INPUT_DIR=$1

OUTPUT_DIR="scenes"

INDEX=0
END=1


mkdir -p $OUTPUT_FILE

for FILE in $INPUT_DIR/*; do
	BASEFILE=$(basename $FILE);
	echo $BASEFILE;
	mkdir -p "${OUTPUT_DIR}/${BASEFILE}";
	csplit -z -f "${OUTPUT_DIR}/${BASEFILE}/" $FILE "/<[LT]>__.*/" {*};
done