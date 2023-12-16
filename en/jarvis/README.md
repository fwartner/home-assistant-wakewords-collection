# Jarvis

Inspired by: [J.A.R.V.I.S.](https://en.wikipedia.org/wiki/J.A.R.V.I.S.)

## jarvis_v2.tflite

This model reacts to `Jarvis` and `Hey Jarvis`.

Use this file if you want less false positives.

### Training

```
number_of_examples = 25000
number_of_training_steps = 500000
false_activation_penalty = 10000
target_words = ["jarvis", "hey jarvis", "jarvis!", "jarvis?"]
```

### Results

```
Final Model Accuracy: 0.6308000087738037
Final Model Recall: 0.26159998774528503
Final Model False Positives per Hour: 0.17699114978313446
```

## jarvis_v1.tflite

This model reacts to `Jarvis` and `Hey Jarvis`.

Use this file if you want more sensitivity.

### Training

```
number_of_examples = 25000
number_of_training_steps = 500000
false_activation_penalty = 2000
target_words = ["jarvis", "hey jarvis", "jarvis!", "jarvis?"]
```

### Results

```
Final Model Accuracy: 0.7590000033378601
Final Model Recall: 0.5235999822616577
Final Model False Positives per Hour: 9.115043640136719
```

## djar_vis.tflite

Unknown
