#!/usr/bin/env python3
# coding: utf-8

import sys
import numpy as np
import keras
from utils import load_embedding
import tensorflow as tf
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
from math import log


PATHS = {
    'word2vec6b': '../data/processed/word2vec.6b.300d.txt',
    'word2vec6b_pickle': '../data/processed/word2vec_model_6b_100.p',
    'word2vec42b': '../data/processed/word2vec.42b.300d.txt',
}


def word2idx(word, w2v_model):
    return w2v_model.vocab[word].index


def idx2word(idx, w2v_model):
    return w2v_model.index2word[idx]


def alt_beam_search_decoder(model, k, seed_text, w2v_model, seq_length,
                            n_words=None):

    # encode the text as integer
    encoded = np.array([word2idx(word, w2v_model) for word in seed_text])
    # truncate sequences to a fixed length
    encoded = pad_sequences([encoded], maxlen=seq_length, truncating='pre')[0]
    # print(encoded.shape)
    sequences = [[encoded, 1.0]]

    # walk over each step in sequence
    for _ in range(n_words):
        all_candidates = list()
        # expand each current candidate
        for seq, score in sequences:
            inp = np.array([seq[-seq_length:]])
            yhat = model.predict(inp, verbose=0)[0]
            prob = yhat / yhat.sum(0)
            indices = np.random.choice(len(w2v_model.vocab), size=k, p=prob)
            for index in indices:
                candidate = [seq + [index], score * -log(yhat[index])]
                all_candidates.append(candidate)

        # order all candidates by score
        ordered = sorted(all_candidates, key=lambda tup: tup[1])
        # select k best
        sequences = ordered[:k]

    return ' '.join([idx2word(i, w2v_model) for i in sequences[0][0]])


# beam search
def beam_search_decoder(model, k, seed_text, w2v_model, seq_length,
                        n_words=None):

    # encode the text as integer
    encoded = np.array([word2idx(word, w2v_model) for word in seed_text])
    # truncate sequences to a fixed length
    encoded = pad_sequences([encoded], maxlen=seq_length, truncating='pre')[0]
    # print(encoded.shape)
    sequences = [[encoded, 1.0]]

    # walk over each step in sequence
    for _ in range(n_words):
        all_candidates = list()
        # expand each current candidate
        for seq, score in sequences:
            inp = np.array([seq[-seq_length:]])
            yhat = model.predict(inp, verbose=0)[0]
            indices = np.argpartition(yhat, -k)[-k:]
            for index in indices:
                candidate = [seq + [index], score * -log(yhat[index])]
                all_candidates.append(candidate)
        # order all candidates by score
        ordered = sorted(all_candidates, key=lambda tup: tup[1])
        # select k best
        sequences = ordered[:k]
    return ' '.join([idx2word(i, w2v_model) for i in sequences[0][0]])


def random_sample(model, seed_text, w2v_model, seq_length, n_words=None):
    result = list()

    # encode the text as integer
    encoded = np.array([word2idx(word, w2v_model) for word in seed_text])

    # truncate sequences to a fixed length
    encoded = pad_sequences([encoded], maxlen=seq_length, truncating='pre')
    # generate a fixed number of words
    for _ in range(n_words):
        # predict probabilities for each word
        yhat = model.predict(encoded, verbose=0)[0]
        prob = yhat / yhat.sum(0)
        index = np.random.choice(len(w2v_model.vocab), p=prob)

        encoded = np.roll(encoded, -1)
        encoded[0][seq_length - 1] = index

        # append to input
        result.append(index)

    return ' '.join([idx2word(i, w2v_model) for i in result])


def main(model_filename):
    # Embedding - Word2Vec
    w2v_model = load_embedding(PATHS['word2vec6b_pickle'], load_pickle=True)

    # load the model
    model = load_model(model_filename)
    # saver = tf.train.Saver()
    # sess = keras.backend.get_session()
    # saver.restore(sess, './keras_model')
    model.summary()
    while(True):
        seed_text = input('Enter the seed text: ')
        if seed_text == 'OUT':
            break
        seed_text = seed_text.split()[:50]
        print(len(seed_text))

        print('Random sample')
        generated = random_sample(model, seed_text, w2v_model, 50, 50)
        print(generated)

        print('\nBeam Search')
        generated = beam_search_decoder(model, 10, seed_text, w2v_model, 50, 50)
        print(generated)

        print('\nRandom Beam Search')
        generated = alt_beam_search_decoder(model, 10, seed_text, w2v_model, 50, 50)
        print(generated)


if __name__ == '__main__':
    model_filename = sys.argv[1]
    main(model_filename)
