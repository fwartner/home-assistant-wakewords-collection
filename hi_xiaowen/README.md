# Hi 小问 (Hi xiǎo wèn)

## hi_xiaowen_v1.tflite

This model reacts to 🇨🇳 `Hi 小问`.

### Training

```
number_of_training_steps = 500000
false_activation_penalty = 5000
```

`positive_train`: 21749 files from [MobvoiHotwords](https://openslr.org/87/) (p_train)

`positive_test`: 1000 files from [MobvoiHotwords](https://openslr.org/87/) (p_test)

`negative_train`: 108624 files from [MobvoiHotwords](https://openslr.org/87/) (n_train) + 10000 synthetic negative files similar to `hi shahwenn`, generated with piper-sample-generator

`negative_test`: 6561 files from [MobvoiHotwords](https://openslr.org/87/) (n_test)

### Results

```
Final Model Accuracy: 0.9094035029411316
Final Model Recall: 0.3190000057220459
Final Model False Positives per Hour: 1.9469026327133179
```

## hi_xiaowen_v2.tflite

This model reacts to 🇨🇳 `Hi 小问`.

### Training

```
number_of_training_steps = 500000
false_activation_penalty = 2000
```

`positive_train`: 21749 files from [MobvoiHotwords](https://openslr.org/87/) (p_train)

`positive_test`: 1000 files from [MobvoiHotwords](https://openslr.org/87/) (p_test)

`negative_train`: 108624 files from [MobvoiHotwords](https://openslr.org/87/) (n_train) + 10000 synthetic negative files similar to `hi shahwenn`, generated with piper-sample-generator

`negative_test`: 6561 files from [MobvoiHotwords](https://openslr.org/87/) (n_test)

### Results

```
Final Model Accuracy: 0.9230260252952576
Final Model Recall: 0.4259999990463257
Final Model False Positives per Hour: 4.77876091003418
```
