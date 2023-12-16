# Hey Potato

## hey_potato.tflite

This model reacts to `Hey Potato` and `Oi Potato`.

### Training

```
number_of_examples = 25000
number_of_training_steps = 500000
false_activation_penalty = 5000
target_words = ["hey potato", "hey potato!", "oi potato", "oy potato!"]
```

### Results

```
Final Model Accuracy: 0.7979999780654907
Final Model Recall: 0.6047999858856201
Final Model False Positives per Hour: 3.805309772491455
```
