#!/bin/bash

INPUT_DIR=$1

OUTPUT_FILE="changes"

INDEX=0
END=1


# for m in movies/*; do ./scene_split.py $m inter/$(basename $m) ; done

# rm "${OUTPUT_FILE}_"*

# for FILE in $INPUT_DIR/*; do
# 	# echo $(basename $FILE);
# 	# ./scene_split.py $FILE >> "${OUTPUT_FILE}_${END}.txt"
# 	if [ "${END}" = "9" ]; then
# 		echo $(basename $FILE) >> "${OUTPUT_FILE}_${END}.txt"
# 		cat $FILE | egrep "^[ \t]+([A-Z]\.?([A-Z\'\"0-9 ]|[A-Z\.])+)( +\([a-zA-Z0-9\(\)\'\"\. ]+\))?$" >> "${OUTPUT_FILE}_${END}.txt"
# 	fi;
# 	# echo "${OUTPUT_FILE}_${END}.txt"
# 	let INDEX=${INDEX}+1
# 	if [ "${INDEX: -2}" = "00" ]; then
# 		let END=${END}+1
# 	fi;
# done

# mkdir $OUTPUT_FILE
# sed -i -E "s/ {5,}[A-Z][0-9]+[A-Z]?$//g" $FILE;

for FILE in $INPUT_DIR/*; do
	BASEFILE=$(basename $FILE);
	echo $BASEFILE;
	sed -i -E "s/^( *)[A-Z][0-9]+[A-Z]? +(.*[^ ]) +[A-Z][0-9]+[A-Z]?$/\1\2/g" $FILE;
	sed -i -E "/^((.*\(MORE\) *?)|(.*CONTINUED.*)|( *\(CONT\.?\).*)|( *[0-9]{1,3}\.))$/d" $FILE;
	sed -i -E "/<\!--/,/-->/d" $FILE;
	sed -i -E "/<b>/,/<\/b>/d" $FILE;
	sed -i -E "/<\/?b>/d" $FILE;
	sed -i '/^\s*$/d' $FILE;
	sed -i -E 's/\s+\*\s*$//g' $FILE;
done

# for FILE in $INPUT_DIR/*; do
# 	BASEFILE=$(basename $FILE);
# 	echo $BASEFILE;
# 	sed -E "s/((FADE|DISSOLVE|CUT) [A-Z ]*)(:)?/\1:\n/g" $FILE > $OUTPUT_FILE/$BASEFILE;
# 	sed -i -E "s/^[ \t]+([A-Z][A-Z\'\"\-\.0-9 ]*) *(\([a-zA-Z0-9\'\"\. ]+\))?$/<CHAR>__{\1} <CHAR_PAR>__{\2}/g" $OUTPUT_FILE/$BASEFILE;
# 	sed -i -E "s/^(INT|EXT|[0-9]+)(.*)$/<LOC>__{\1\2}/g" $OUTPUT_FILE/$BASEFILE;
# 	sed -i -E "s/^ *([A-Z ]+:)$/<TRANS>__{\1}/g" $OUTPUT_FILE/$BASEFILE;
# 	sed -i -E "s/^ {5,}((\(.*)|([^\)]+\)))$/<DIAL_PAR>__{\1}/g" $OUTPUT_FILE/$BASEFILE;
# 	sed -i -E "s/^ {5,}(.*)$/<DIAL>__{\1}/g" "${OUTPUT_FILE}/${BASEFILE}";
# 	sed -i -E "s/^([A-Z ]+)$/<ACTION_ALT>__{\1}/g" "${OUTPUT_FILE}/${BASEFILE}";
# 	sed -i -E "s/^([^<].*)+$/<ACTION>__{\1}/g" "${OUTPUT_FILE}/${BASEFILE}";
# done

# rm "locs_.txt";
# for FILE in $INPUT_DIR/*; do
# 	# echo $(basename $FILE);
# 	# ./scene_split.py $FILE >> "${OUTPUT_FILE}_${END}.txt"
# 		echo $(basename $FILE) >> "locs_.txt";
# 		cat $FILE | egrep "^<TRANS>__.*?$" >> "locs_.txt";
# 	# echo "${OUTPUT_FILE}_${END}.txt"
# done