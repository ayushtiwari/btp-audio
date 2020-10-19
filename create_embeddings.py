import glob
import os
import pickle
import json
import tensorflow_hub as hub

embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")

paths = glob.glob('./output/*')

for path in paths:
    print("Processing {}".format(path))
    comb_vocab_path = os.path.join(path, 'combined_vocab.json')

    with open(comb_vocab_path, 'r') as f:
        combined = json.load(f)

    savepath = os.path.join(path, "embeddings.pickle")

    embeddings = dict()

    for speaker in combined:
        embeddings[speaker] = embed([combined[speaker]])

    with open(savepath, 'wb') as f:
        pickle.dump(embeddings, f)
