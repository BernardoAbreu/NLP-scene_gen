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
	if [ "${END}" = "5" ]; then
		echo $(basename $FILE) >> "${OUTPUT_FILE}_${END}.txt"
		cat $FILE | egrep "^[ \t]+([A-Z]\.?([A-Z\'\"0-9 ]|[A-Z\.])+)( +\([a-zA-Z0-9\(\)\'\"\. ]+\))?$" >> "${OUTPUT_FILE}_${END}.txt"
	fi;
	# echo "${OUTPUT_FILE}_${END}.txt"
	let INDEX=${INDEX}+1
	if [ "${INDEX: -2: 2}" = "00" ]; then
		let END=${END}+1
	fi;
done
