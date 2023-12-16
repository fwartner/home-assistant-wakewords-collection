# Ok Paulus

Inspired by: [Paulus](https://www.nabucasa.com/about/), Founder of Home Assistant

## ok_paulus.tflite

This model reacts to `Okay Paulus`.

### Training

```
number_of_examples = 25000
number_of_training_steps = 500000
false_activation_penalty = 5000
target_words = ["ok paulus", "ok powlus", "ok powlus?", "ok powlus!"]
```

### Results

```
Final Model Accuracy: 0.8356000185012817
Final Model Recall: 0.6796000003814697
Final Model False Positives per Hour: 4.955751895904541
```
