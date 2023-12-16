# Wheatley

Inspired by: [Wheatley](https://en.wikipedia.org/wiki/Wheatley_(Portal))

## wheatley.tflite

This model reacts to `Wheatley` and `Hey Wheatley`.

### Training

```
number_of_examples = 25000
number_of_training_steps = 500000
false_activation_penalty = 5000
target_words = ["wheatley", "wheatley!", "wheatley?", "hey wheatley!"]
```

### Results

```
Final Model Accuracy: 0.6792307496070862
Final Model Recall: 0.3407999873161316
Final Model False Positives per Hour: 2.38938045501709
```
