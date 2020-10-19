import glob
import os
import json
import pickle

paths = glob.glob('/Users/ayushtiwari/Desktop/btp-audio/output/*')

for path in paths:
    print('Processing {}'.format(path))

    count_file = os.path.join(path, 'interruptions.json')
    with open(count_file, 'r') as f:
        interruptions = json.load(f)

    anchor_file = os.path.join(path, 'anchor.json')
    with open(anchor_file, 'r') as f:
        anchor = json.load(f)

    tuples = dict()

    for guest_a in interruptions:
        for guest_b in interruptions:
            if guest_a != guest_b and \
                    (anchor, guest_b, guest_a) not in tuples and \
                    (anchor, guest_a, guest_b) not in tuples:
                if interruptions[guest_a] >= interruptions[guest_b]:
                    tuples[(anchor, guest_a, guest_b)] = 1
                else:
                    tuples[(anchor, guest_a, guest_b)] = 0

    savepath = os.path.join(path, 'tuples.pickle')
    with open(savepath, 'wb') as f:
        pickle.dump(tuples, f)