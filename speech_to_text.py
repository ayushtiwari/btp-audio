import glob
import os
import json

import speech_recognition as sr

paths = glob.glob('/home/btp-souvic/HULK/ayushtiwari/output/*')
audio_dir = '/home/btp-souvic/HULK/ayushtiwari/train-audios'

r = sr.Recognizer()

for path in paths:
    mapping_file_path = os.path.join(path, 'mapping.json')

    with open(mapping_file_path, 'r') as f:
        mapping = json.load(f)

    identifier = os.path.basename(path)
    audio_path = os.path.join(audio_dir, '{}'.format(identifier))
    print("Processing {}".format(audio_path))

    savepath = os.path.join(path, 'vocab.json')

    vocab = dict()

    for speaker in mapping:
        print("Translating Spekaer {}".format(speaker))
        vocab[speaker] = []
        for interval in mapping[speaker]["intervals"]:
            start_time = float(interval[0])
            duration = float(interval[1]) - float(interval[0])

            print(start_time, duration)

            audio_file = sr.AudioFile(audio_path)
            with audio_file as source:
                audio = r.record(source, offset=start_time, duration=duration)
                vocab[speaker].append(r.recognize_sphinx(audio))
                print(vocab[speaker][-1])

    with open(savepath, 'w') as f:
        json.dump(vocab, f, indent=4, sort_keys=True)
