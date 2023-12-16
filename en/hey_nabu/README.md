# Hey Nabu

Inspired by: [Nabu Casa](https://www.nabucasa.com/)

## hey_nabu_v2.tflite

This model reacts to `Hey Nabu` and `Okay Nabu`.

Use this file if you want less false positives.

### Training

```
number_of_examples = 25000
number_of_training_steps = 500000
false_activation_penalty = 20000
target_words = ["hey nabu", "ok nabu"]
```

### Results

```
Final Model Accuracy: 0.7904000282287598
Final Model Recall: 0.5839999914169312
Final Model False Positives per Hour: 1.0619468688964844
```

## hey_nabu_v1.tflite

This model reacts to `Hey Nabu` and `Okay Nabu`.

Use this file if you want more sensitivity.

### Training

```
number_of_examples = 25000
number_of_training_steps = 500000
false_activation_penalty = 5000
target_words = ["hey nabu", "ok nabu"]
```

### Results

```
Final Model Accuracy: 0.8256000280380249
Final Model Recall: 0.6567999720573425
Final Model False Positives per Hour: 3.185840606689453
```
