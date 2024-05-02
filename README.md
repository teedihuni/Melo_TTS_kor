<div align="center">
  <div>&nbsp;</div>
  <img src="logo.png" width="300"/> 
</div>

## Introduction
MeloTTS is a **high-quality multi-lingual** text-to-speech library by [MyShell.ai](https://myshell.ai). Supported languages include:

TTS test (language KOREA)

### step 1 
you need to download weight in [melo hugginface](https://huggingface.co/myshell-ai/MeloTTS-Korean/tree/main).
also config.json need to be downloaded.

### step 2
```
cd melo
python infer.py -t "<TEXT EXAMPLES>" -m "<weigth_path>" -o "<result_path>" -l 'KR'
```

you can also change voice speed.
original infer.py do not use voice speed arguments but default speed is too slow for korea language.
So just added speed arguments to customize. speed 1.2 fits well in korean voice.


```
python infer.py -t "<TEXT EXAMPLES>" -m "<weigth_path>" -o "<result_path>" -l 'KR' -sp 1.3
```








## Usage
- [Use without Installation](docs/quick_use.md)
- [Install and Use Locally](docs/install.md)
- [Training on Custom Dataset](docs/training.md)

The Python API and model cards can be found in [this repo](https://github.com/myshell-ai/MeloTTS/blob/main/docs/install.md#python-api) or on [HuggingFace](https://huggingface.co/myshell-ai).

**Citation**
```
@software{zhao2024melo,
  author={Zhao, Wenliang and Yu, Xumin and Qin, Zengyi},
  title = {MeloTTS: High-quality Multi-lingual Multi-accent Text-to-Speech},
  url = {https://github.com/myshell-ai/MeloTTS},
  year = {2023}
}
```

## License

This library is under MIT License, which means it is free for both commercial and non-commercial use.

## Acknowledgements

This implementation is based on [TTS](https://github.com/coqui-ai/TTS), [VITS](https://github.com/jaywalnut310/vits), [VITS2](https://github.com/daniilrobnikov/vits2) and [Bert-VITS2](https://github.com/fishaudio/Bert-VITS2). We appreciate their awesome work.
