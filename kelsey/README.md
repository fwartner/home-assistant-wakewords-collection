# Kelsey

## kelsey.tflite

This model reacts to `Kelsey` and `Hey Kelsey`.

### Training

```
number_of_examples = 25000
number_of_training_steps = 500000
false_activation_penalty = 5000
target_words = ["kelsey", "kelsey!", "kelsey?", "hey kelsey"]
```

### Results

```
Final Model Accuracy: 0.7013999819755554
Final Model Recall: 0.41200000047683716
Final Model False Positives per Hour: 2.1238937377929688
```
