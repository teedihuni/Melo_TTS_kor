from melo.api import TTS
from melo.text.korean import normalize
import os
import glob
import sys
import re
import time

language = 'KR'
base_path = f'{os.getcwd()}/test'
model = TTS(language=language)

speaker_ids = model.hps.data.spk2id
speakers = list(speaker_ids.keys())

root_folder = language.lower()
if 'zh' in root_folder:
    pass
    texts = open('basetts_test_resources/zh_mix_en_egs_text.txt', 'r').readlines()
    language = 'ZH_MIX_EN'
elif 'es' in root_folder:
    pass
    texts = open('basetts_test_resources/es_egs_text.txt', 'r').readlines()
    language = 'SP'
elif 'fr' in root_folder:
    pass
    texts = open('basetts_test_resources/fr_egs_text.txt', 'r').readlines()
    language = 'FR'
elif 'en' in root_folder:
    pass
    texts = open('basetts_test_resources/en_egs_text.txt', 'r').readlines()
    # texts = ["Boss? You're not my boss, you're just a sad little person who likes to hide behind a computer screen and pretend you have power over others. "]
    language = 'EN'
elif 'jp' in root_folder:
    pass
    texts = open('basetts_test_resources/jp_egs_text.txt', 'r').readlines()
    language = 'JP'
elif 'kr' in root_folder:
    texts = open(os.path.join(base_path,'basetts_test_resources/kr_egs_text.txt'),'r').readlines()  
    texts = [normalize(text) for text in texts]
    language = 'KR'
else:
    raise NotImplementedError()

save_dir = os.path.join(base_path,'basetts_outputs_package', root_folder.split('/')[-1])

for speed in [1.1]:
    for speaker in speakers:
        for sent_id, text in enumerate(texts):
            output_path = f'{save_dir}/{speaker}/speed_{speed}/sent_{sent_id:03d}.wav'
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            start_time = time.time()
            model.tts_to_file(text, speaker_ids[speaker], output_path, speed=speed)
            end_time = time.time()
            print(end_time - start_time)