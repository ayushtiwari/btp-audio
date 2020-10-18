import glob
import os
import json

paths=glob.glob('/home/btp-souvic/HULK/ayushtiwari/output/*')

for path in paths:
    print('Processing {}'.format(path))
    rttm = os.path.join(path, 'rttm.txt')
    with open(rttm, 'r') as f:
       lines = [line.rstrip() for line in f.readlines()]

    mapping = dict()
    prev_speaker = None

    for line in lines:
        data = line.split(' ')
        speaker = data[7]
        stime = float(data[3])
        ftime = float(data[3]) + float(data[4])

        if not speaker in mapping:
            mapping[speaker] = []

        if prev_speaker==speaker:
            mapping[speaker][-1][1] = ftime

        else:
            mapping[speaker].append([stime, ftime])

        prev_speaker = speaker
    
    for speaker in mapping:
        old_intervals=mapping[speaker]
        new_intervals=[]
        duration=0.0
        for interval in old_intervals:
            if (interval[1]-interval[0] >= 5.0):
                new_intervals.append(interval)
                duration+=interval[1]-interval[0]
        
        mapping[speaker]={'duration': duration, 'intervals': new_intervals}

    savepath = os.path.join(path, 'mapping.json')
    with open(savepath, 'w') as f:
        json.dump(mapping, f, indent=4, sort_keys=True)
