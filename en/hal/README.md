# HAL

Inspired by: [HAL 9000](https://en.wikipedia.org/wiki/HAL_9000)

## hal_v1.tflite

This model reacts to `HAL`.

Use this file if you want more sensitivity.

### Training

```
number_of_examples = 25000
number_of_training_steps = 500000
false_activation_penalty = 10000
target_words = ["hal", "hal?", "hal!"]
```

### Results

```
Final Model Accuracy: 0.7049999833106995
Final Model Recall: 0.41440001130104065
Final Model False Positives per Hour: 3.274336338043213
```

## hal_v2.tflite

This model reacts to `HAL`.

Use this file if you want less false positives.

### Training

```
number_of_examples = 25000
number_of_training_steps = 500000
false_activation_penalty = 100000
target_words = ["hal", "hal?", "hal!"]
```

### Results

```
Final Model Accuracy: 0.593999981880188
Final Model Recall: 0.188400000333786
Final Model False Positives per Hour: 0.08849557489156723
```
