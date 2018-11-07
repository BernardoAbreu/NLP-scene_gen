#!/bin/bash

INPUT_DIR=$1

OUTPUT_FILE="changes"

INDEX=0
END=1


# for FILE in inter/*; do
# 	BASEFILE=$(basename $FILE);
# 	echo $BASEFILE;
# 	./scene_split.py $FILE "inter2/${BASEFILE}";
# done

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

mkdir -p $OUTPUT_FILE
# sed -i -E "s/ {5,}[A-Z][0-9]+[A-Z]?$//g" $FILE;

# for FILE in $INPUT_DIR/*; do
# 	BASEFILE=$(basename $FILE);
# 	echo $BASEFILE;
# 	# sed -i -E "s/^( *)[A-Z][0-9]+[A-Z]? +(.*[^ ]) +[A-Z][0-9]+[A-Z]?$/\1\2/g" $FILE;
# 	# sed -i -E "s/ (INT|EXT) /\1./g" $FILE
# 	# sed -i -E "s/^[0-9]+[A-Z]?\s+(INT|EXT)\./\1./g" $FILE
# 	# sed -i -E "s/\s\s+[0-9]+[A-Z]?\.?$//g" $FILE;
# 	# sed -i -E "/^((.*\(MORE\) *?)|(.*CONTINUED.*)|( *\(CONT\.?\).*)|( *[0-9]{1,3}\.))$/d" $FILE;
# 	# sed -i -E "s/((FADE|DISSOLVE|CUT) [A-Z ]*)(:)?/\1:\n/g" $FILE;
# 	# sed -i -E "s/((NIGHT|DAY|AFTERNOON|TWILIGHT) )/\1\n/g" $FILE;
# 	sed -i -E "/<\!--/,/-->/d" $FILE;
# 	sed -i -E "/<b>/,/<\/b>/d" $FILE;
# 	sed -i -E "/<\/?b>/d" $FILE;
# 	sed -i '/^\s*$/d' $FILE;
# 	sed -i -E 's/\s+\*?\s*$//g' $FILE;
	# sed -i -E "s/[\^~]//g" $FILE;
 #    sed -i -E "s/[0-9]+EXT([\. ])/EXT\1/g" $FILE;
 #    sed -i -E "s/[0-9]+INT([\. ])/INT\1/g" $FILE;
 #    sed -i -E "s/([\.\,\!\"\?:\;])/ \1 /g" $FILE;
# done

# for FILE in $INPUT_DIR/*; do
# 	BASEFILE=$(basename $FILE);
# 	echo $BASEFILE;
# 	sed -E "s/^[ \t]+([A-Z][A-Z\'\"\-\.0-9 ]*) *(\([a-zA-Z0-9\'\"\. ]+\))?$/<CHAR>__{\L\1}\n\U<CHAR_PAR>__{\L\2}/g" "${FILE}" > "${OUTPUT_FILE}/${BASEFILE}";
# 	sed -i -E "s/^(INT|EXT|[0-9]+)(.*)?$/<LOC>__{\L\1\2}/g" "${OUTPUT_FILE}/${BASEFILE}";
# 	sed -i -E "s/^ *([A-Z ]+:)$/<TRANS>__{\L\1}/g" "${OUTPUT_FILE}/${BASEFILE}";
# 	sed -i -E "s/^ {4,}((\(.*)|([^\)]+\)))$/<DIAL_PAR>__{\L\1}/g" "${OUTPUT_FILE}/${BASEFILE}";
# 	sed -i -E "s/^\s{4,}(.*)$/<DIAL>__{\L\1}/g" "${OUTPUT_FILE}/${BASEFILE}";
# 	sed -i -E "s/^\s*([A-Z \-\.]+)$/<ACTION_ALT>__{\L\1}/g" "${OUTPUT_FILE}/${BASEFILE}";
# 	sed -i -E "s/^\s*([^<].*)+$/<ACTION>__{\L\1}/g" "${OUTPUT_FILE}/${BASEFILE}";
# done


# for FILE in $INPUT_DIR/*; do
# 	BASEFILE=$(basename $FILE);
# 	echo $BASEFILE;
# 	sed -i -E ":begin;$!N;s/^(<LOC>__\{[^\n]*) *\}\n<LOC>__\{([^\n]*\})/\1 \2/;tbegin;P;D" changes/$BASEFILE;
# 	sed -i -E ":begin;$!N;s/^(<TRANS>__\{[^\n]*) *\}\n<TRANS>__\{([^\n]*\})/\1 \2/;tbegin;P;D" changes/$BASEFILE;
# 	sed -i -E ":begin;$!N;s/^(<ACTION>__\{[^\n]*) *\}\n<ACTION>__\{([^\n]*\})/\1 \2/;tbegin;P;D" changes/$BASEFILE;
# 	sed -i -E ":begin;$!N;s/^(<ACTION_ALT>__\{[^\n]*) *\}\n<ACTION_ALT>__\{([^\n]*\})/\1 \2/;tbegin;P;D" changes/$BASEFILE;
# 	sed -i -E ":begin;$!N;s/^(<DIAL_PAR>__\{[^\n]*) *\}\n<DIAL_PAR>__\{([^\n]*\})/\1 \2/;tbegin;P;D" changes/$BASEFILE;
# 	sed -i -E ":begin;$!N;s/^(<DIAL>__\{[^\n]*) *\}\n<DIAL>__\{([^\n]*\})/\1 \2/;tbegin;P;D" changes/$BASEFILE;
# done;


for FILE in $INPUT_DIR/*; do
	BASEFILE=$(basename $FILE);
	echo $BASEFILE;
	# sed -i -E "s/^<LOC>__/<L>__/g" changes/$BASEFILE;
	# sed -i -E "s/^<TRANS>__/<T>__/g" changes/$BASEFILE;
	# sed -i -E "s/^<ACTION>__/<A>__/g" changes/$BASEFILE;
	# sed -i -E "s/^<ACTION_ALT>__/<B>__/g" changes/$BASEFILE;
	# sed -i -E "s/^<DIAL>__/<D>__/g" changes/$BASEFILE;
	# sed -i -E "s/^<DIAL_PAR>__/<P>__/g" changes/$BASEFILE;
	# sed -i -E "s/^<CHAR>__/<C>__/g" changes/$BASEFILE;
	# sed -i -E "s/^<CHAR_PAR>__/<E>__/g" changes/$BASEFILE;
	# sed -i '/<E>__{}$/d' changes/$BASEFILE;
	sed -i -E 's/\^\~/ /g' changes/$BASEFILE;
	sed -i -E 's/[\-\-]/ /g' changes/$BASEFILE;
	sed -i -E 's/[\\\-\/]/ /g' changes/$BASEFILE;
	sed -i -E 's/\s+/ /g' changes/$BASEFILE;
	sed -i -E "s/i'll/i will/g" changes/$BASEFILE;
done;

# rm "locs_.txt";
# for FILE in $INPUT_DIR/*; do
# 	# echo $(basename $FILE);
# 	# ./scene_split.py $FILE >> "${OUTPUT_FILE}_${END}.txt"
# 		echo $(basename $FILE) >> "locs_.txt";
# 		cat $FILE | egrep "^<TRANS>__.*?$" >> "locs_.txt";
# 	# echo "${OUTPUT_FILE}_${END}.txt"
# done

# rm "locs_.txt";
# for FILE in changes/*; do
# 	echo $(basename $FILE);
# 	# ./scene_split.py $FILE >> "${OUTPUT_FILE}_${END}.txt"
# 	echo $(basename $FILE) >> "locs_.txt";
# 		cat $FILE | egrep "^<LOC>__.*?$" | wc -l >> locs_.txt
# 	# echo "${OUTPUT_FILE}_${END}.txt"
# done
