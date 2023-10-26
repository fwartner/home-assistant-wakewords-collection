# GLaDOS

Inspired by: [GLaDOS](https://en.wikipedia.org/wiki/GLaDOS)

## glados.tflite

This model reacts to `Glados` and `Hey Glados`.

### Training

```
number_of_examples = 25000
number_of_training_steps = 500000
false_activation_penalty = 5000
target_words = ["glados", "glàdos", "glàdos!", "glàdos?", "hey glàdos", "hey glàdos!"]
```

### Results

```
Final Model Accuracy: 0.7856000065803528
Final Model Recall: 0.574400007724762
Final Model False Positives per Hour: 4.2477874755859375
```
