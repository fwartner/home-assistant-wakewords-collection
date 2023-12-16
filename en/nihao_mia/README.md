# 你好米雅 (Nǐ hǎo mǐ yǎ)

## nihao_mia_v2.tflite

This model reacts to 🇨🇳 `你好米雅`.

### Training

```
number_of_training_steps = 1000000
false_activation_penalty = 20000
```

`positive_train`: 106128 files from the [HI-MIA](https://www.openslr.org/85/) dataset

`positive_test`: 2000 files from the [HI-MIA](https://www.openslr.org/85/) dataset

`negative_train`: 16343 files from the [HI-MIA-CW](https://www.openslr.org/120/) dataset + 25000 synthetic negative files similar to `neehao mia`, generated with piper-sample-generator

`negative_test`: 2500 synthetic negative files similar to `neehao mia`, generated with piper-sample-generator

### Results

```
Final Model Accuracy: 0.7446666955947876
Final Model Recall: 0.42649999260902405
Final Model False Positives per Hour: 2.654867172241211
```

## nihao_mia_v1.tflite

This model reacts to 🇨🇳 `你好米雅`.

### Training

```
number_of_training_steps = 500000
false_activation_penalty = 20000
```

`positive_train`: 106128 files from the [HI-MIA](https://www.openslr.org/85/) dataset

`positive_test`: 2000 files from the [HI-MIA](https://www.openslr.org/85/) dataset

`negative_train`: 16343 files from the [HI-MIA-CW](https://www.openslr.org/120/) dataset + 25000 synthetic negative files similar to `neehao mia`, generated with piper-sample-generator

`negative_test`: 2500 synthetic negative files similar to `neehao mia`, generated with piper-sample-generator

### Results

```
Final Model Accuracy: 0.6882222294807434
Final Model Recall: 0.2985000014305115
Final Model False Positives per Hour: 0.17699114978313446
```
