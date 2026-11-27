# Alexa

This model reacts to `Alexa`. It is an Apache 2.0 replacement for the `alexa` model that comes with openWakeWord, which is licensed CC BY-NC-SA 4.0.

Source: [13fragments/wakeword-alexa-en](https://huggingface.co/13fragments/wakeword-alexa-en), tag `v1.0.2`. The files in this folder equal that release.

## alexa_v1.tflite

Threshold: 0.487, calibrated for at most 0.5 false accepts per hour. The add-on default is 0.5.

Copy `alexa_v1.tflite` into `/share/openwakeword` and restart the openWakeWord add-on. The add-on drops the `_v1` suffix, so this file replaces the bundled `alexa` model. It runs on the Home Assistant server; Voice PE and other ESPHome devices cannot load it. Tested with `wyoming-openwakeword` 2.1.0, the server in add-on 2.1.0 and 2.1.1.

### Training

- Positives: 20,000 synthetic clips of "Alexa" and 10,000 clips of similar words from the Piper voice `en_US-libritts-high` (MIT), which was trained on LibriTTS (CC BY 4.0).
- Negatives: LibriSpeech `train-clean-100` (CC BY 4.0) and FSD50K noise clips (CC0 1.0 and CC BY 3.0).
- Recipe: the `openwakeword` training defaults (DNN, layer size 32, 50,000 steps). It did not use the Colab notebook.

### Results

Test data: the 329 `alexa` clips of the Picovoice wake-word benchmark, and 82.25 hours of AMI and DiPCo speech without the wake word.

| Model | False rejects | False accepts per hour |
|---|---|---|
| This model | 0.91 % | 0.523 |
| Mean of 4 training seeds | 1.69 % | 0.377 |
| microWakeWord v2 `alexa` | 1.22 % | 0.571 |

These results do not show that this model is better than microWakeWord. The seed mean trails it by 0.47 points (95 % interval −1.08 to +1.99).

### Licence

These files are licensed Apache 2.0; see `LICENSE` and `NOTICE` in this folder. The MIT licence of the collection covers the other folders.

SHA-256:

- `alexa_v1.onnx`: `f8a87c0038ad0fc66c9ad544d214ae706daf45cba38ee5503d63f263a61fe41d`
- `alexa_v1.tflite`: `0bbefbec84e4da51095ea31560b9606e075c543c493209e086cba880049bfbf5`

Amazon, Alexa, and all related marks are trademarks of Amazon.com, Inc. or its affiliates. Amazon is not affiliated with this model and does not endorse it.
