# Computer

Inspired by: [LCARS](https://en.wikipedia.org/wiki/LCARS)

## computer_v2.tflite

This model reacts to `Computer` and `Hey Computer`.

### Training

```
number_of_examples = 25000
number_of_training_steps = 500000
false_activation_penalty = 5000
target_words = ["khom-pioodr", "khom-pioodr!", "khom-pioodr?", "khom-pioota", "khom-pioota!", "khom-pyoota?", "hey computer", "hey computer?", "hey computer!"]
```

1437 files added to `positive_train`:

411*3 files (computer) from https://github.com/Picovoice/wake-word-benchmark

58*3 files (computer/en) from https://github.com/MycroftAI/Precise-Community-Data

10*3 files (heycomputer/en) from https://github.com/MycroftAI/Precise-Community-Data

### Results

```
Final Model Accuracy: 0.7833999991416931
Final Model Recall: 0.5703999996185303
Final Model False Positives per Hour: 5.221238613128662
```

## computer_v1.tflite

This model reacts to `Computer` and `Hey Computer`.

### Training

```
number_of_examples = 25000
number_of_training_steps = 500000
false_activation_penalty = 5000
target_words = ["khom-pioodr", "khom-pioodr!", "khom-pioodr?", "khom-pioota", "khom-pioota!", "khom-pyoota?", "hey computer", "hey computer?", "hey computer!"]
```

### Results

```
Final Model Accuracy: 0.7832000255584717
Final Model Recall: 0.573199987411499
Final Model False Positives per Hour: 4.69026517868042
```
