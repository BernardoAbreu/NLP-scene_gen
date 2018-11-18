#!/bin/bash

INPUT_DIR=$1

for SCENE in $INPUT_DIR*; do
	echo "" >> $SCENE;
	sed -i '/^\s*$/d' $SCENE;
done;

echo "Done!!!";
