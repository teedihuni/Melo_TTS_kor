

## For korean TTS

Just using melotts in korea texts

### step 1 Install 
The repo is developed and tested on `Ubuntu 20.04` and `Python 3.9`.

```
pip install -e 
python -m unidic download
```

### step 2 Weight download
you need to download weight in [melo hugginface](https://huggingface.co/myshell-ai/MeloTTS-Korean/tree/main).

'config.json' also need to be downloaded.


### step 3 Inference

# method 1
```
cd melo
python infer.py -t "<TEXT EXAMPLES>" -m "<weigth_path>" -o "<result_path>" -l 'KR'
```

you can also change voice speed.

original infer.py do not use voice speed arguments but default speed is too slow for korea language.

So i just added speed arguments to customize. Speed 1.2 fits well in korean voice.

```
python infer.py -t "<TEXT EXAMPLES>" -m "<weigth_path>" -o "<result_path>" -l 'KR' -sp 1.3
```

# method 2
```
cd test
python test_base_model_tts_package.py
```

if you use this method you need to add config$checkpoint arguments when you define TTS model.

not just like this 'model = TTS(language=language)' but 'model = TTS(language=language, config_path=config_path, ckpt_path=ckpt_path)'

### launch.json example for vscode debug 
```
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python Debugger: Current File",
            "type": "debugpy",
            "request": "launch",
            "program": "${file}",
            "args": [
                "-t","안녕하세요 TTS 품질 테스트 중입니다. 중요한 요소라고 생각되는 음성, 목소리, 어조를 유심히 살펴봐주시기 바랍니다.",
                "-m","MeloTTS/melo/weight/checkpoint.pth",
                "-o","MeloTTS/test/result",
                "-l","KR",
                "-sp","1.23"

            ],
            "console": "integratedTerminal",
            "justMyCode": false
        }

    ]
}
```


### todo list
* [X] inference test  [2024.05.02]
* [X] voice speed  [2024.05.02]
* [ ] train test



<div align="center">
  <div>&nbsp;</div>
  <img src="logo.png" width="300"/> 
</div>

## Introduction
MeloTTS is a **high-quality multi-lingual** text-to-speech library by [MyShell.ai](https://myshell.ai). Supported languages include:

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
