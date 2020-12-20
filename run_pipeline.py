import glob
import os
import json

import torch

audio_dir = '/home/btp-souvic/HULK/ayushtiwari/urban_debates'
output_dir = '/home/btp-souvic/HULK/ayushtiwari/btp-audio/output_urban_debates'

pipeline = torch.hub.load('pyannote/pyannote-audio', 'dia')

for path in glob.glob(audio_dir + '/*'):
    identifier = os.path.basename(path).split('.')[0]
    print("Processing {}".format(identifier))

    savepath = os.path.join(output_dir, identifier)
    rttm_savepath = os.path.join(savepath, 'rttm.txt')
    chart_savepath = os.path.join(savepath, 'chart.json')

    if not os.path.exists(savepath):
        os.mkdir(savepath)

    info = {'uri': identifier, 'audio': path}

    diarization = pipeline(info)

    with open(rttm_savepath, 'w') as fp:
        diarization.write_rttm(fp)

    with open(chart_savepath, 'w') as fp:
        json.dump(diarization.chart(), fp)
