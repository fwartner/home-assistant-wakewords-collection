# Hey Snips

Inspired by: [Snips Voice Assistant](https://snips.ai/), acquired by Sonos

## hey_snips.tflite

This model reacts to `Hey Snips`.

### Training

```
number_of_examples = 25000
number_of_training_steps = 500000
false_activation_penalty = 5000
target_words = ["hey snips"]
```

### Results

```
Final Model Accuracy: 0.7942000031471252
Final Model Recall: 0.5952000021934509
Final Model False Positives per Hour: 6.902654647827148
```
