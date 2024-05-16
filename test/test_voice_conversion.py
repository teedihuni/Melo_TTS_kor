## cuda issues

from melo.api import TTS
from melo.text.korean import normalize
import os
import time
import torch
from openvoice import se_extractor
from openvoice.api import ToneColorConverter

base_path = f'{os.getcwd()}'

# initialization
ckpt_converter = f'{base_path}/melo/weight/checkpoints_v2/converter'
device = "cuda:0" if torch.cuda.is_available() else "cpu"
output_dir = 'outputs_v2'

tone_color_converter = ToneColorConverter(f'{ckpt_converter}/config.json', device=device)
tone_color_converter.load_ckpt(f'{ckpt_converter}/checkpoint.pth')

os.makedirs(output_dir, exist_ok=True)


# tone color embedding (reference_spearker = vocic you want to clone)
reference_speaker = f'{base_path}/test/resources/conversion_test.wav'
target_se, audio_name = se_extractor.get_se(reference_speaker, tone_color_converter, vad=False)


language = 'KR'
source_path = f'{os.getcwd()}/test'
model = TTS(language=language, device= device)

speaker_ids = model.hps.data.spk2id
speakers = list(speaker_ids.keys())

root_folder = language.lower()

save_dir = os.path.join(source_path, output_dir, root_folder.split('/')[-1])
src_path = os.path.join(source_path, 'resources/conversion_test.wav')

for speed in [1.1]:
    for speaker in speakers:
        output_path = f'{save_dir}/{speaker}/conversion_result.wav'
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        start_time = time.time()

        source_se = torch.load(f'{base_path}/melo/weight/checkpoints_v2/base_speakers/ses/{root_folder}.pth', map_location=device)
        
        encode_message = "@MyShell" 
        tone_color_converter.convert(
            audio_src_path=src_path, 
            src_se=source_se, 
            tgt_se=target_se, 
            output_path=output_path,
            message=encode_message)


        end_time = time.time()
        print(end_time - start_time)