#!/bin/bash

INPUT_DIR=$1

while read -r line ; do
	MOVIE=$line;
	echo -ne "${MOVIE} \033[0K\r";
	mv "all_scenes/regular/sentences/${MOVIE}" "all_scenes/regular/test_sentences/";
	mv "all_scenes/regular/tags/${MOVIE}_tags" "all_scenes/regular/test_tags/";
	mv "all_scenes/no_punct/sentences/${MOVIE}_np" "all_scenes/no_punct/test_sentences/";
	mv "all_scenes/no_punct/tags/${MOVIE}_tags_np" "all_scenes/no_punct/test_tags/";
	mv "all_scenes/no_stop/sentences/${MOVIE}_ns" "all_scenes/no_stop/test_sentences/";
	mv "all_scenes/no_stop/tags/${MOVIE}_tags_ns" "all_scenes/no_stop/test_tags/";
done < "$INPUT_DIR";
