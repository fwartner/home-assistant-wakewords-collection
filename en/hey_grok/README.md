# Hey Grok

## hey_grok.tflite

This model reacts to `Hey Grok`. Tested on M5Stack Atom Echo with the
openWakeWord add-on. Recommended threshold: 0.5 (lower to ~0.4 if it misses you).

### Training

Trained with openWakeWord via the community Colab notebook
(openwakeword-colab-2026 / wakeword_trainer_HA).

```
target_phrase = ["hey grok", "hey grock"]
n_samples = 2000
steps = 20000
max_negative_weight = 1500
```

### Results

```
Best Validation Accuracy: 0.869
Best Validation Recall: 0.750
Best False Positives per Hour: 0.15
```

### Notes

Trained on datasets with mixed licenses; for non-commercial personal use only.
Not affiliated with or endorsed by xAI. "Grok" is a trademark of xAI.
