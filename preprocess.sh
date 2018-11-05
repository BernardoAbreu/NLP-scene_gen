#!/bin/bash

INPUT_DIR=$1

OUTPUT_DIR="tagged"


mkdir -p $OUTPUT_DIR


# # Convert to lowercase
# for FILE in $INPUT_DIR/*; do
# 	BASEFILE=$(basename $FILE);
# 	echo $BASEFILE;
# 	sed -E "s/(<[A-Z]+>__)(\{[^\}]*\})/\1\L\2/g" $FILE > $OUTPUT_DIR/$BASEFILE;
# done;


# REMOVE extra spaces
for FILE in $INPUT_DIR/*; do
	BASEFILE=$(basename $FILE);
	echo $BASEFILE;
	sed -E "s/\s\+/ /g" $FILE > $OUTPUT_DIR/$BASEFILE;
	sed -E -i "s/\s\+\}/ /g" $OUTPUT_DIR/$BASEFILE;
done;