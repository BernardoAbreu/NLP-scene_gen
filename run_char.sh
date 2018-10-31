#!/bin/bash

INPUT_DIR=$1

OUTPUT_FILE="character_list"

INDEX=0
END=1


# for m in movies/*; do ./scene_split.py $m inter/$(basename $m) ; done

rm "${OUTPUT_FILE}_"*

for FILE in $INPUT_DIR/*; do
	# echo $(basename $FILE);
	# ./scene_split.py $FILE >> "${OUTPUT_FILE}_${END}.txt"
	if [ "${END}" = "9" ]; then
		echo $(basename $FILE) >> "${OUTPUT_FILE}_${END}.txt"
		cat $FILE | egrep "^[ \t]+([A-Z]\.?([A-Z\'\"0-9 ]|[A-Z\.])+)( +\([a-zA-Z0-9\(\)\'\"\. ]+\))?$" >> "${OUTPUT_FILE}_${END}.txt"
	fi;
	# echo "${OUTPUT_FILE}_${END}.txt"
	let INDEX=${INDEX}+1
	if [ "${INDEX: -2}" = "00" ]; then
		let END=${END}+1
	fi;
done



for FILE in $INPUT_DIR/*; do
	BASEFILE=$(basename $FILE);
	echo $BASEFILE;
	sed -E "/^((.*\(MORE\) *?)|( *\(CONT\.?\).*)|( *[0-9]{1,3}\.))$/d" $FILE > changes/$BASEFILE
	sed -i 's/ +\*?$//' changes/$BASEFILE;
	sed -i '/^\s*$/d' changes/$BASEFILE;
	sed -E -i "s/^[ \t]+([A-Z][A-Z\'\"\.0-9 ]*) *(\([a-zA-Z0-9\'\"\. ]+\))?$/<CHAR>__{\1} <CHAR_PAR>__{\2}/" changes/$BASEFILE;
	sed -E -i "s/^(INT|EXT|[0-9]+)(.*)$/<LOC>__{\1\2}/" changes/$BASEFILE;
	# sed -E"s/^[ \t]+([A-Z][A-Z\'\"\.0-9 ]*) *(\([a-zA-Z0-9\'\"\. ]+\))?$/<CHAR>__{\1} <CHAR_PAR>__{\2}/" $FILE > chars/$BASEFILE;
done