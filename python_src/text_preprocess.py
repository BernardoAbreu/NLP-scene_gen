#!/usr/bin/env python3

import nltk
from nltk.corpus import stopwords
from utils import load_embedding
from utils import split_movies
from utils import read_text
from utils import save_sequences
import sys

# nltk.download('punkt')
# nltk.download('stopwords')

PATHS = {
    'word2vec': '~/NLP-scene_gen/data/processed/word2vec.6b.100d.txt',
    'word2vec_pickle': 'data/processed/word2vec_model_6b_100.p',
}

SENTENCE_LENGTH = 50
STOPWORDS_SET = set(stopwords.words('english'))


def preprocess(w2v_model, movie_file, out_filename):
    # Read movie file
    movie = read_text(movie_file)

    # Tokenize each sentence
    movie_tokens = [(t[0], nltk.tokenize.word_tokenize(t[1])) for t in movie]

    movie_no_stopwords = []
    for t, m_list in movie_tokens:
        new_movie = (t, [m for m in m_list if m not in STOPWORDS_SET])
        if new_movie[1]:
            movie_no_stopwords.append(new_movie)

    regextokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
    movie_no_punct = [(t[0], regextokenizer.tokenize(t[1])) for t in movie]

    # Split movie and get list of tags
    tokens, tags = split_movies(movie_tokens, w2v_model)
    tokens_no_stop, tags_no_stop = split_movies(movie_no_stopwords, w2v_model)
    tokens_no_punct, tags_no_punct = split_movies(movie_no_punct, w2v_model)

    # Organize into sequences of tokens
    sequences = [ngram for ngram in nltk.ngrams(tokens, SENTENCE_LENGTH + 1)]
    # print('Total Sequences: %d' % len(sequences))
    tags_sequences = [ngram
                      for ngram in nltk.ngrams(tags, SENTENCE_LENGTH + 1)]
    # print('Total Tag sequences: %d' % len(tags_sequences))

    sequences_no_stop = [ngram for ngram in nltk.ngrams(tokens_no_stop,
                                                        SENTENCE_LENGTH + 1)]
    # print('Total Sequences: %d' % len(sequences_no_stop))
    tags_sequences_no_stop = [ngram
                              for ngram in nltk.ngrams(tags_no_stop,
                                                       SENTENCE_LENGTH + 1)]
    # print('Total Tag sequences: %d' % len(tags_sequences_no_stop))

    sequences_no_punct = [ngram
                          for ngram in nltk.ngrams(tokens_no_punct,
                                                   SENTENCE_LENGTH + 1)]
    # print('Total Sequences: %d' % len(sequences_no_punct))
    tags_sequences_no_punct = [ngram
                               for ngram in nltk.ngrams(tags_no_punct,
                                                        SENTENCE_LENGTH + 1)]
    # print('Total Tag sequences: %d' % len(tags_sequences_no_punct))

    # Save sequences to file
    save_sequences(out_filename, sequences)
    save_sequences(out_filename + '_tags', tags_sequences)

    save_sequences(out_filename + '_ns', sequences_no_stop)
    save_sequences(out_filename + '_tags_ns', tags_sequences_no_stop)

    save_sequences(out_filename + '_np', sequences_no_punct)
    save_sequences(out_filename + '_tags_np', tags_sequences_no_punct)


if __name__ == '__main__':
    # movie_file = sys.argv[1]
    # out_filename = sys.argv[2]

    # Load word2vec
    w2v_model = load_embedding(PATHS['word2vec_pickle'], load_pickle=True)
    # preprocess(w2v_model, movie_file, out_filename)
    with open('all_scenes.txt', 'r') as f:
        scenes = [line.rstrip() for line in f]

    CURSOR_UP_ONE = '\033[F'
    ERASE_LINE = '\033[K'
    total = len(scenes)
    total = '/' + str(total)
    for i, scene in enumerate(scenes):
        out_filename = 'all_scenes/' + '_'.join(scene.split('/')[-2:])
        s = str(i) + total + ' - ' + out_filename
        print(s)
        preprocess(w2v_model, scene, out_filename)
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(ERASE_LINE)
    print('Done')
