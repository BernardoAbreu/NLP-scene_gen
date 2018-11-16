#!/bin/bash

INPUT_DIR=$1

for MOVIE in "${INPUT_DIR}*"; do
	for SCENE in $MOVIE/*; do
		echo "${SCENE}" >> all_scenes.txt;
	done;
done;