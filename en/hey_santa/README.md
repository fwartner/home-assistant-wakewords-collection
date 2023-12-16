# Hey Santa

## hey_santa.tflite

This model reacts to `Hey Santa` and `Santa`.

### Training

```
number_of_examples = 25000
number_of_training_steps = 500000
false_activation_penalty = 5000
target_words = ["hey santa", "hey santa!", "hey santa?", "santa!"]
```

### Results

```
Final Model Accuracy: 0.7347999811172485
Final Model Recall: 0.47920000553131104
Final Model False Positives per Hour: 4.8672566413879395
```
