# Hey Alba

Inspired by: [Alba speech corpus](https://datashare.ed.ac.uk/handle/10283/3270) which is available as a model in piper: https://huggingface.co/rhasspy/piper-voices/tree/main/en/en_GB/alba/medium

## hey_alba.tflite

This model reacts to `Hey Alba` with both English and Scottish pronunciations.

### Training

```
number_of_examples = 25000
number_of_training_steps = 500000
false_activation_penalty = 5000
target_words = ["hey alba", "hey alba!", "hey al_abuh", "hey al_abuh!"]
```

### Results

```
Final Model Accuracy: 0.8142389345541564
Final Model Recall: 0.5726391137101814
Final Model False Positives per Hour: 3.7633289183616184
```
