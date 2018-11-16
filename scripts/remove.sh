#!/bin/bash

INPUT_DIR=$1

# for m in scenes/*; do
# 	echo $m >> 00.txt;
# 	cat $m/00 >> 00.txt;
# 	echo '\n'>> 00.txt;
# done;

# cat 00.txt | while read line; do rm $line/00; done


for MOVIE in "${INPUT_DIR}*"; do
	for SCENE in $MOVIE/*; do
		echo $SCENE;
		sed -i '/^\s*$/d' $SCENE;
	done;
done;


# rm count.txt;
# for MOVIE in "${INPUT_DIR}*"; do
# 	for SCENE in $MOVIE/*; do
# 		COUNT=$(cat $SCENE | wc -w);
# 		if [ $COUNT -lt 70 ]; then
# 			echo "${SCENE}: ${COUNT}" >> count.txt;
# 		fi
# 	done;
# done;

# for MOVIE in "${INPUT_DIR}*"; do
# 	echo $MOVIE;
# 	for SCENE in $MOVIE/*; do
# 		if [ -f $SCENE ]; then
# 			COUNT=$(cat $SCENE | wc -w);
# 		else
# 			COUNT=71;
# 		fi;

# 		if [ $COUNT -lt 70 ]; then
# 			echo "${SCENE} ${COUNT}";
# 			FILE=$(basename $SCENE);
# 			COUNT2="$((10#${FILE}+4))";
# 			cat "${MOVIE}/"$(printf "%02d" $((10#$COUNT2))) >> "${MOVIE}/"$(printf "%02d" $((10#$FILE)));
# 			rm "${MOVIE}/"$(printf "%02d" $((10#$COUNT2))) || rm "${MOVIE}/"$(printf "%02d" $((10#$FILE)));
# 		fi;
# 	done;
# done;
