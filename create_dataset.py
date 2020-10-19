import glob
import os
import json
import pickle

import numpy as np

paths = glob.glob('/Users/ayushtiwari/Desktop/btp-audio/output/*')

features = []
labels = []

for path in paths:
    print('Processing {}'.format(path))

    tuples_file = os.path.join(path, 'tuples.pickle')
    with open(tuples_file, 'rb') as f:
        tuples = pickle.load(f)

    embeddings_file = os.path.join(path, 'embeddings.pickle')
    with open(embeddings_file, 'rb') as f:
        embeddings = pickle.load(f)

    for key in tuples:
        anchor = key[0]
        guest_a = key[1]
        guest_b = key[2]

        feature = [embeddings[anchor], embeddings[guest_a], embeddings[guest_b]]
        label = tuples[key]

        features.append(feature)
        labels.append(label)

features_arr = np.array(features)
labels_arr = np.array(labels, dtype=int)

savepath = 'dataset'
features_savepath = os.path.join(savepath, 'features.pickle')
labels_savepath = os.path.join(savepath, 'labels.pickle')

print("Saving...")

with open(features_savepath, 'wb') as f:
    pickle.dump(features_arr, f)

with open(labels_savepath, 'wb') as f:
    pickle.dump(labels_arr, f)

print(features_arr.shape)
print(labels_arr.shape)
    #
    #
    # savepath = os.path.join(path, 'tuples.pickle')
    # with open(savepath, 'wb') as f:
    #     pickle.dump(tuples, f)