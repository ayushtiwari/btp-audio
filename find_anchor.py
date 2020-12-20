import glob
import os
import json

paths = glob.glob('/home/btp-souvic/HULK/ayushtiwari/btp-audio/output_urban_debates/*')

for path in paths:
    mapping_file_path = os.path.join(path, 'mapping.json')

    print("Processing {}".format(path))

    with open(mapping_file_path, 'r') as f:
        mapping = json.load(f)

    savepath = os.path.join(path, 'anchor.json')

    candidate = ''
    max_duration = 0
    for speaker in mapping:
        duration = mapping[speaker]["duration"]
        if duration > max_duration:
            candidate = speaker
            max_duration = duration

    with open(savepath, 'w') as f:
        json.dump(candidate, f)
