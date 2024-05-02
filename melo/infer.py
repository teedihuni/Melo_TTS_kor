import os
import click
from melo.api import TTS

'''
python infer.py --text "<some text here>" -m /path/to/checkpoint/G_<iter>.pth -o <output_dir>

python infer.py -t '안녕하세요. 티티에스 품질 100% 테스트 중입니다. 중요한 요소라고 생각되는 음성, 목소리, 어조를 유심히 살펴봐주시기 바랍니다.' 
                -m ./weight/checkpoint.pth -o ../test -l 'KR' -sp 1.23
'''
    
@click.command()
@click.option('--ckpt_path', '-m', type=str, default=None, help="Path to the checkpoint file")
@click.option('--text', '-t', type=str, default=None, help="Text to speak")
@click.option('--language', '-l', type=str, default="EN", help="Language of the model")
@click.option('--output_dir', '-o', type=str, default="outputs", help="Path to the output")
@click.option('--voice_speed' ,'-sp' , type=float, default = 1.0, help='Voice Speed')
def main(ckpt_path, text, language, output_dir, voice_speed):
    if ckpt_path is None:
        raise ValueError("The model_path must be specified")
    
    config_path = os.path.join(os.path.dirname(ckpt_path), 'config.json')
    model = TTS(language=language, config_path=config_path, ckpt_path=ckpt_path)
    
    for spk_name, spk_id in model.hps.data.spk2id.items():
        save_path = f'{output_dir}/{spk_name}/output.wav'
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        model.tts_to_file(text, spk_id, save_path, speed = voice_speed)

if __name__ == "__main__":
    main()
