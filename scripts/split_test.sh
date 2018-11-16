#!/bin/bash

INPUT_DIR=$1

while read -r line ; do
	MOVIE=$line;
	echo $MOVIE;
	mv "all_scenes/regular/test_sentences/${MOVIE}" "all_scenes/regular/sentences/";
	mv "all_scenes/regular/test_tags/${MOVIE}_tags" "all_scenes/regular/tags/";
	mv "all_scenes/no_punct/test_sentences/${MOVIE}_np" "all_scenes/no_punct/sentences/";
	mv "all_scenes/no_punct/test_tags/${MOVIE}_tags_np" "all_scenes/no_punct/tags/";
	mv "all_scenes/no_stop/test_sentences/${MOVIE}_ns" "all_scenes/no_stop/sentences/";
	mv "all_scenes/no_stop/test_tags/${MOVIE}_tags_ns" "all_scenes/no_stop/tags/";
done < "$INPUT_DIR";
