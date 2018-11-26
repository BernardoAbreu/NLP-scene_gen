#!/usr/bin/env python3

import pandas as pd
from utils import load_embedding
import keras
import tensorflow as tf
import sys


PATHS = {
    'word2vec6b': '../data/processed/word2vec.6b.300d.txt',
    'word2vec6b_pickle': '../data/processed/word2vec_model_6b_100.p',
    'word2vec42b': '../data/processed/word2vec.42b.300d.txt',
}


# load doc into memory
def load_doc(filename):
    # open the file as read only
    file = open(filename, 'r')
    # read all text
    text = file.read()
    # close the file
    file.close()
    return text


tagdict = {'T': 0, 'A': 1, 'B': 2, 'D': 3, 'P': 4, 'C': 5, 'L': 7}


def tag2id(tag):
    return tagdict[tag]


def main(train_filename, train_tags_filename, test_filename, test_tags_filename):
    save_name = train_filename.split('/')[-1]

    # Embedding - Word2Vec
    w2v_model = load_embedding(PATHS['word2vec6b_pickle'], load_pickle=True)

    print('Load')
    # load
    df_train = pd.read_csv(train_filename, sep=' ', prefix='X', header=None)
    length = df_train.shape[1]
    df_train.rename(columns={'X' + str(length - 1): 'Y'}, inplace=True)

    df_test = pd.read_csv(test_filename, sep=' ', prefix='X', header=None)
    df_test.rename(columns={'X' + str(length - 1): 'Y'}, inplace=True)

    df_train_tags = pd.read_csv(train_tags_filename, sep=' ', prefix='X',
                                header=None)
    df_train_tags.rename(columns={'X' + str(length - 1): 'Y'}, inplace=True)

    df_test_tags = pd.read_csv(test_tags_filename, sep=' ', prefix='X',
                               header=None)
    df_test_tags.rename(columns={'X' + str(length - 1): 'Y'}, inplace=True)

    print('integer encode sequences of words')
    # integer encode sequences of words

    def word2idx(word):
        return w2v_model.vocab[word].index

    df_train = df_train.applymap(word2idx)
    df_test = df_test.applymap(word2idx)
    df_train_tags = df_train_tags.applymap(tag2id)
    df_test_tags = df_test_tags.applymap(tag2id)

    print('separate into input and output')
    # separate into input and output
    train_X = df_train.drop('Y', axis=1)
    train_Y = df_train['Y']
    train_tags_X = df_train_tags.drop('Y', axis=1)
    test_tags_X = df_test_tags.drop('Y', axis=1)

    SENTENCE_LENGTH = train_X.shape[1]

    test_X = df_test.drop('Y', axis=1)
    test_Y = df_test['Y']

    print('Define model')
    # define model
    # model = keras.models.Sequential()

    # ### Adiciona camada de embedding
    vocab_size, embedding_size = w2v_model.vectors.shape

    input1 = keras.layers.Input(shape=(SENTENCE_LENGTH,))
    embed_layer = keras.layers.Embedding(input_dim=vocab_size,
                                         output_dim=embedding_size,
                                         input_length=(SENTENCE_LENGTH),
                                         weights=[w2v_model.vectors])(input1)

    lstm1 = keras.layers.LSTM(50, return_sequences=True)(embed_layer)
    lstm2 = keras.layers.LSTM(50)(lstm1)

    intags = keras.layers.Input(shape=(SENTENCE_LENGTH,))

    cc1 = keras.layers.concatenate([lstm2, intags], axis=1)

    dense1 = keras.layers.Dense(50, activation='relu')(cc1)
    dense2 = keras.layers.Dense(vocab_size, activation='softmax')(dense1)

    model = keras.models.Model(inputs=[input1, intags], outputs=dense2)
    print(model.summary())

    print('Compile model')
    # compile model
    model.compile(loss='sparse_categorical_crossentropy',
                  optimizer='adam', metrics=['accuracy'])

    print('Begin training')
    # fit model
    csv_logger = keras.callbacks.CSVLogger('training.log')
    early_stop = keras.callbacks.EarlyStopping(monitor='val_loss',
                                               min_delta=0.001,
                                               patience=4,
                                               verbose=1,
                                               mode='min')
    filepath = save_name + "_weights.best.hdf5"
    checkpoint = keras.callbacks.ModelCheckpoint(filepath, monitor='val_acc',
                                                 verbose=1,
                                                 save_best_only=True,
                                                 mode='max')

    model.fit([train_X, train_tags_X], train_Y, batch_size=64, epochs=1,
              callbacks=[csv_logger, early_stop, checkpoint])

    # save the model to file
    saver = tf.train.Saver()
    sess = keras.backend.get_session()
    saver.save(sess, './' + save_name + 'keras_model')
    model.save(train_filename + '_model.h5')

    print('Evaluating model:')
    scores = model.evaluate([test_X, test_tags_X], test_Y)
    print("Test model %s: %.2f%%" % (model.metrics_names[1], scores[1] * 100))


if __name__ == '__main__':
    train_filename = sys.argv[1]
    train_tags_filename = sys.argv[2]
    test_filename = sys.argv[3]
    test_tags_filename = sys.argv[4]
    main(train_filename, train_tags_filename,
         test_filename, test_tags_filename)
