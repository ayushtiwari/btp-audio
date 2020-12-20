import glob
import os
import json

paths = glob.glob('/home/btp-souvic/HULK/ayushtiwari/btp-audio/output_urban_debates/*')

for path in paths:
    print('Processing {}'.format(path))
    rttm = os.path.join(path, 'rttm.txt')
    with open(rttm, 'r') as f:
        lines = [line.rstrip() for line in f.readlines()]

    anchor_file = os.path.join(path, 'anchor.json')

    with open(anchor_file, 'r') as f:
        anchor = json.load(f)

    count = dict()
    prev_speaker = None

    for line in lines:
        data = line.split(' ')
        speaker = data[7]

        if prev_speaker:
            if speaker == anchor and prev_speaker != anchor:
                if prev_speaker in count:
                    count[prev_speaker] += 1
                else:
                    count[prev_speaker] = 1

        prev_speaker = speaker

    savepath = os.path.join(path, 'interruptions.json')
    with open(savepath, 'w') as f:
        json.dump(count, f, indent=4, sort_keys=True)
