#!/bin/bash

INPUT_DIR=$1

OUTPUT_FILE="out_words"

rm $OUTPUT_FILE;

for FILE in $INPUT_DIR/*; do
	BASEFILE=$(basename $FILE);
	echo $BASEFILE;
	sed -E "s/(.*)/\L\1/g" $FILE >> $OUTPUT_FILE;
done;

sed -i -E "s/\s\+/ /g" $OUTPUT_FILE;
sed -i -E "s/\s/\n/g" $OUTPUT_FILE;
sed -i '/^\s*$/d' $OUTPUT_FILE;
sed -i -E "s/\'s/ is/g" $OUTPUT_FILE;
sed -i -E 's/[\,\.\?\:\!\;\-\"\(\)]//g' $OUTPUT_FILE;
sed -i -E "s/'(.*)'/\1/g" $OUTPUT_FILE;
# sed -i -E "s/(.*)/\L\1/g" $OUTPUT_FILE;
# # sed -i -E 
# # sed -i -E "s/([^A-Za-z ])([A-Za-z])/\1 \2/g" $OUTPUT_FILE;


# sed -i -E "s/\'re/\nare/g" $OUTPUT_FILE;
# sed -i -E "s/\'ve/\nhave/g" $OUTPUT_FILE;
# sed -i -E "s/\'m/\nam/g" $OUTPUT_FILE;

# sed -i -E "s/'re/ are/g" out_words;
# sed -i -E "s/'ve/ have/g" out_words;
# sed -i -E "s/'m/ am/g" out_words;
# sed -i -E "s/'ll/ will/g" out_words;
# sed -i -E "s/'d/ would/g" out_words;

# sed -i -E "s/\s/\n/g" out_words
# sed -i '/^\s*$/d' out_words

cat $OUTPUT_FILE | sort | uniq -c | sort -V > count_words;
cat count_words | egrep -E "^\s+1 .*" > single;
