import gensim
import pickle


def load_embedding(filename, load_pickle=False):
    if load_pickle:
        m = pickle.load(open(filename, 'rb'))
    else:
        m = gensim.models.KeyedVectors.load_word2vec_format(filename)
        pickle.dump(m, open(filename + '.p', 'wb'))
    return m


def split_movies(movie_tokens, w2v_model):
    tokens = []
    tags = []
    for tag, seq in movie_tokens:
        block = [word for word in seq if word in w2v_model.vocab]
        tokens.extend(block)
        tags.extend(([tag] * len(block)))
    return tokens, tags


# ## Leitura do texto
def read_text(filename):
    with open(filename, 'r') as f:
        movie = [(line[1], line[6:-2]) for line in f]

    return [t if t[0] not in ('P, E') else (t[0], t[1][1:-1]) for t in movie]


def save_sequences(out_filename, sequences):
    with open(out_filename, 'w') as f:
        f.write('\n'.join([' '.join(line) for line in sequences]))
