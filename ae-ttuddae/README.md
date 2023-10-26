# ae-ttuddae

Inspired by: [Better Things](https://www.youtube.com/watch?v=TforiqSzgEo&t=713s)

## ae-ttuddae.tflite

This model reacts to `ae-ttuddae`.

### Training

```
number_of_examples = 25000
number_of_training_steps = 500000
false_activation_penalty = 5000
target_words = ["i tootdeh", "i tootdeh!", "i tûtdée", "i tûtdée!"]
target_words_negative = ["i-tootdeh"]
```

### Results

```
Final Model Accuracy: 0.8266666531562805
Final Model Recall: 0.6615384817123413
Final Model False Positives per Hour: 2.4778759479522705
```
