# Hey KITT

Inspired by: [K.I.T.T.](https://en.wikipedia.org/wiki/KITT)

## hey_kitt.tflite

This model reacts to `Hey KITT` and `Okay KITT`.

### Training

```
number_of_examples = 25000
number_of_training_steps = 500000
false_activation_penalty = 10000
target_words = ["hey kitt", "hey kitt!", "okay kitt", "okay kitt!"]
```

### Results

```
Final Model Accuracy: 0.722599983215332
Final Model Recall: 0.4487999975681305
Final Model False Positives per Hour: 1.1504424810409546
```
