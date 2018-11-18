#!/bin/bash

INPUT_DIR=$1

for SCENE in $INPUT_DIR*; do
	MOVIE=$(basename $SCENE);
	echo $MOVIE;
	cat "all_scenes/regular/sentences/${MOVIE}" >> net_data/movies_sentences.txt;
	#cat "all_scenes/regular/test_tags/${MOVIE}_tags" >> net_data/test_movies_tags.txt;
	cat "all_scenes/no_punct/sentences/${MOVIE}_np" >> net_data/movies_sentences_np.txt;
	#cat "all_scenes/no_punct/test_tags/${MOVIE}_tags_np" >> net_data/test_movies_tags_np.txt;
	cat "all_scenes/no_stop/sentences/${MOVIE}_ns" >> net_data/movies_sentences_ns.txt;
	#cat "all_scenes/no_stop/test_tags/${MOVIE}_tags_ns" >> net_data/test_movies_tags_ns.txt;
done;
