# Hey Frenck

Inspired by: [Frenck](https://www.youtube.com/channel/UCZ2Ku6wrhdYDHCaBzLaA3bw)

## hey_frenck.tflite

This model reacts to `Hey Frenck` and `Okay Frenck`.

### Training

```
number_of_examples = 25000
number_of_training_steps = 500000
false_activation_penalty = 5000
target_words = ["hey frenck", "hey frank", "ok frenck", "ok frank"]
```

### Results

```
Final Model Accuracy: 0.8198000192642212
Final Model Recall: 0.6444000005722046
Final Model False Positives per Hour: 2.7433629035949707
```
