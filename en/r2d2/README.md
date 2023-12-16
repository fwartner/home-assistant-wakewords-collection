# R2-D2

Inspired by: [R2-D2](https://en.wikipedia.org/wiki/R2-D2)

## r2d2.tflite

This model reacts to `R2-D2`.

### Training

```
number_of_examples = 25000
number_of_training_steps = 500000
false_activation_penalty = 5000
target_words = ["r two d two"]
```

### Results

```
Final Model Accuracy: 0.8381999731063843
Final Model Recall: 0.6812000274658203
Final Model False Positives per Hour: 4.69026517868042
```
