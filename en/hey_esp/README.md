# Hey ESP

Inspired by: [ESP32](https://en.wikipedia.org/wiki/ESP32)

## hey_esp.tflite

This model reacts to `Hey ESP` and `Okay ESP`.

### Training

```
number_of_examples = 25000
number_of_training_steps = 500000
false_activation_penalty = 5000
target_words = ["hey e s p", "hey e s p!", "ok e s p", "ok e s p!"]
target_words_negative = ["hey eehespee", "ok eehespee"]
```

### Results

```
Final Model Accuracy: 0.7914000153541565
Final Model Recall: 0.5852000117301941
Final Model False Positives per Hour: 3.9823007583618164
```
