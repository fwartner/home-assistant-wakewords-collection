# Em ơi!

If you sit in any Vietnamese Cafe, you will hear shouts of “Em ơi!”
every few minutes. It is an expression that literally translates to
“Hey younger sister!” or “Hey younger brother!” — but it is used to
get the attention of anyone who is younger than you, like “excuseme
me, Miss!?”

Although it's a Vietnamese expression, it's also often used byforeigners
foreigners to call a waiter/waitress, so I decided to train it and add
to Home Assistant's English wake words.

## Training

Number_of_examples = 25000
number_of_training_steps = 500000
False_activation_penalty = 500000
Target_words = [ "em__oi!" ]

## Results

Final Model Accuracy: 0.8269000053405762
Final Model Recall: 0.6543999910354614
Final Model False Positives per Hour: 2.8318583965301514
