# Choo Choo Homie

Inspired by: [Frenck](https://www.youtube.com/channel/UCZ2Ku6wrhdYDHCaBzLaA3bw)

## choo_choo_homie.tflite

This model reacts to `Choo Choo Homie`.

### Training

```
number_of_examples = 25000
number_of_training_steps = 500000
false_activation_penalty = 5000
target_words = ["choo choo homie", "choo choo homie!"]
```

### Results

```
Final Model Accuracy: 0.8519999980926514
Final Model Recall: 0.7099999785423279
Final Model False Positives per Hour: 5.7522125244140625
```
