#!/usr/bin/env python
# coding: utf-8

# In[306]:


import re

import numpy as np
import pandas as pd
import keras
import sklearn
import nltk
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
import gensim
from nltk.corpus import stopwords
from random import randint

nltk.download('punkt')
nltk.download('stopwords')


# ## LOAD DATA

# ### Load movie

# In[378]:


filename = '../changes/10thingsihateaboutyou.txt'

with open(filename, 'r') as f:
    movie = [(line[1],line[6:-2]) for line in f]

movie = [t if t[0] not in ('P, E') else (t[0],t[1][1:-1]) for t in movie]
print(len(movie))


# ##### Tokenize each sentence

# In[379]:


movie_tokens = [(t[0], nltk.tokenize.word_tokenize(t[1])) for t in movie]
# movie_no_stopwords = []
# for t, m_list in movie_tokens:
#     new_movie = (t, [m for m in m_list if m not in set(stopwords.words('english'))])
#     if new_movie[1]:
#         movie_no_stopwords.append(new_movie)
# regextokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
# movie_no_punct = [(t[0], regextokenizer.tokenize(t[1])) for t in movie]


# In[382]:


print(movie_tokens[50])
print(len(movie_tokens))


# ## Load word2vec

# In[4]:


w2v_model = gensim.models.KeyedVectors.load_word2vec_format("../data/processed/word2vec.6b.100d.txt")


# In[6]:


import pickle
pickle.dump(w2v_model, open('../data/processed/word2vec_model_6b_300.p', 'wb'))


# ##### Split movie and get list of tags

# In[383]:


def split_movies(movie_tokens):
    tokens = []
    tags = []
    for tag, seq in movie_tokens:
        block = [word for word in seq if word in w2v_model.vocab]
        tokens.extend(block)
        tags.extend(([tag]*len(block)))
    return tokens, tags


# In[384]:


tokens, tags = split_movies(movie_tokens)


# ### Organize into sequences of tokens

# In[385]:


SENTENCE_LENGTH = 50
sequences = [list(ngram) for ngram in nltk.ngrams(tokens, SENTENCE_LENGTH + 1)]
print('Total Sequences: %d' % len(sequences))
print(sequences[1])


# ### Save sequences to file

# In[386]:


out_filename = 'movie_sequences.txt'
with open(out_filename, 'w') as f:
    f.write('\n'.join([' '.join(line) for line in sequences]))


# ### Load sequences from file

# In[387]:


in_filename = 'movie_sequences.txt'
df_seq = pd.read_csv(in_filename, sep=' ', prefix='X', header=None)
df_seq.rename(columns={'X'+ str(length - 1): 'Y'}, inplace=True)
print(df_seq.shape)


# In[388]:


df_seq.head()


# ### Integer encode sequences of words

# In[389]:


print(df_seq.shape)


# In[390]:


def word2idx(word):
    return w2v_model.vocab[word].index


# In[391]:


df_seq = df_seq.applymap(word2idx)
df_seq.head()


# ### Separate input and output

# In[392]:


X = df_seq.drop('Y', axis=1)
Y = df_seq['Y']
print(X.shape)
print(Y.shape)
print(len(w2v_model.vocab))


# ## Model Architecture

# In[393]:


model = keras.models.Sequential()
model


# ### Add Embedding Layer

# In[394]:


vocab_size, embedding_size = w2v_model.vectors.shape

model.add(
    keras.layers.Embedding(
        input_dim=vocab_size,
        output_dim=embedding_size,
        input_length=(SENTENCE_LENGTH),
        weights=[w2v_model.vectors]
        
    )
)


# ### Add LSTM Layers

# In[395]:


model.add(keras.layers.LSTM(50, return_sequences=True))
model.add(keras.layers.LSTM(50))
model.add(keras.layers.Dense(50, activation='relu'))
model.add(keras.layers.Dense(vocab_size, activation='softmax'))


# In[396]:


print(model.summary())


# In[397]:


print('Compile model')
# compile model
model.compile(loss='sparse_categorical_crossentropy',
              optimizer='adam', metrics=['accuracy'])


# In[403]:


print('Begin training')
# fit model
model.fit(X, Y, batch_size=64, epochs=2)


# In[407]:


model.save('model.h5')


# In[190]:


def idx2word(idx):
    return w2v_model.index2word[idx]


# In[404]:


def generate_seq(model, seq_length, seed_text, n_words):
    result = list()
    in_text = seed_text
#     print(seed_text)
    # generate a fixed number of words
    for _ in range(n_words):
        # encode the text as integer
        encoded = np.array([word2idx(word) for word in in_text])
        # truncate sequences to a fixed length
        encoded = pad_sequences([encoded], maxlen=seq_length, truncating='pre')
        # predict probabilities for each word
        yhat = model.predict([encoded], verbose=0)
        possibilites
        prob = yhat[0] / yhat[0].sum(0)
        index = np.random.choice(len(w2v_model.vocab), p=prob)
#         # map predicted word index to word
        out_word = idx2word(index)
#         # append to input
        in_text.append(out_word)
        result.append(out_word)
    return ' '.join(result)


# In[405]:


seed_text = sequences[randint(0,len(sequences))][:50]
print(seed_text)


# In[406]:


generated = generate_seq(model, 50, seed_text[:50], 50)
print(' '.join(seed_text) + ' ' + generated)

