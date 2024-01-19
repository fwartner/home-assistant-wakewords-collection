# Hey Barabas

Inspired by: [Barabas](https://en.wikipedia.org/wiki/Professor_Barabas)

## hey_barabas.tflite

This model reacts to `Hey Barabas`.

### Training

```
number_of_examples = 1000
number_of_training_steps = 10000
false_activation_penalty = 1500
target_word = "hey_barrhra_bas"
```

Used training data from English TTS, hence the `target_word` formulation; the wakeword model may be improved by using Dutch or Flemish instead.