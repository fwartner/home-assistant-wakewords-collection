# Oi Fuckwhit

## oi_fuckwhit_v1.tflite

This model reacts to `Oi Fuckwhit`.

Use this file if you want more sensitivity.

### Training

```
number_of_examples = 1000
number_of_training_steps = 10000
false_activation_penalty = 1500
```

### Results

```
Final Model Accuracy: 0.7210000157356262
Final Model Recall: 0.44200000166893005
Final Model False Positives per Hour: 1.8584070205688477
```

## oi_fuckwhit_v2.tflite

This model reacts to `Oi Fuckwhit`.

Use this file if you want less false positives.

### Training

```
number_of_examples = 30000
number_of_training_steps = 20000
false_activation_penalty = 1500
```

### Results

```
Final Model Accuracy: 0.6973333358764648
Final Model Recall: 0.3946666717529297
Final Model False Positives per Hour: 0.44247788190841675
```
