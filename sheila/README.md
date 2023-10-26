# Sheila

## sheila_v2.tflite

This model reacts to `Sheila`.

### Training

```
number_of_examples = 25000
number_of_training_steps = 500000
false_activation_penalty = 5000
target_words = ["sheila", "sheila!", "sheila?"]
```

1734 files from the [Google Speech Commands Dataset](https://blog.research.google/2017/08/launching-speech-commands-dataset.html) added to `positive_train`

### Results

```
Final Model Accuracy: 0.7314000129699707
Final Model Recall: 0.4708000123500824
Final Model False Positives per Hour: 2.38938045501709
```

## sheila_v1.tflite

This model reacts to `Sheila`.

### Training

```
number_of_examples = 25000
number_of_training_steps = 500000
false_activation_penalty = 5000
target_words = ["sheila", "sheila!", "sheila?"]
```

### Results

```
Final Model Accuracy: 0.7268000245094299
Final Model Recall: 0.45840001106262207
Final Model False Positives per Hour: 3.539823055267334
```
