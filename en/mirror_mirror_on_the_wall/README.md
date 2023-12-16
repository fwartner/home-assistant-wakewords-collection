# Mirror mirror on the wall

Inspired by: [Magic Mirror](https://en.wikipedia.org/wiki/Magic_Mirror_(Snow_White))

## mirror_mirror_on_the_wall.tflite

This model reacts to `Mirror mirror on the wall` and `Magic mirror on the wall`.

### Training

```
number_of_examples = 25000
number_of_training_steps = 500000
false_activation_penalty = 30000
target_words = ["mirror mirror on the wall", "magic mirror on the wall"]
```

### Results

```
Final Model Accuracy: 0.8327999711036682
Final Model Recall: 0.6660000085830688
Final Model False Positives per Hour: 3.008849620819092
```

## mirror_mirror.tflite

This model reacts to `Mirror Mirror`.

### Training

```
number_of_examples = 25000
number_of_training_steps = 500000
false_activation_penalty = 5000
target_words = ["mirror mirror", "mirror mirror!", "mirrörmirrör"]
```

### Results

```
Final Model Accuracy: 0.8155999779701233
Final Model Recall: 0.6380000114440918
Final Model False Positives per Hour: 5.840707778930664
```
