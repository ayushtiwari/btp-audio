import glob
import os
import json

paths = glob.glob('/Users/ayushtiwari/Desktop/btp-audio/output/*')

for path in paths:

    print("Processing {}".format(path))
    vocab_file_path = os.path.join(path, 'vocab.json')

    with open(vocab_file_path, 'r') as f:
        vocab = json.load(f)

    combined = dict()

    for speaker in vocab:
        combined[speaker] = ' '.join(vocab[speaker])

    savepath = os.path.join(path, 'combined_vocab.json')

    with open(savepath, 'w') as f:
        json.dump(combined, f, indent=4, sort_keys=True)
