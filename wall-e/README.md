# WALL-E

Inspired by: [WALL-E](https://en.wikipedia.org/wiki/WALL-E)

## wall-e.tflite

This model reacts to `WALL-E` and `Hey WALL-E`.

### Training

```
number_of_examples = 25000
number_of_training_steps = 500000
false_activation_penalty = 5000
target_words = ["wallie", "wallie?", "wallie!", "hey wallie"]
```

### Results

```
Final Model Accuracy: 0.7414000034332275
Final Model Recall: 0.48840001225471497
Final Model False Positives per Hour: 3.451327323913574
```
