# Hey Rick

Inspired by: [Rick Sanchez](https://en.wikipedia.org/wiki/Rick_Sanchez)

## hey_rick.tflite

This model reacts to `Hey Rick`.

### Training

```
number_of_examples = 25000
number_of_training_steps = 500000
false_activation_penalty = 5000
target_words = ["hey rick", "hey rick!"]
```

### Results

```
Final Model Accuracy: 0.7300000190734863
Final Model Recall: 0.46399998664855957
Final Model False Positives per Hour: 0.7079645991325378
```
