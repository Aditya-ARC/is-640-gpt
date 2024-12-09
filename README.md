## is-640-gpt 
Let's build GPT

"data.py”: read data from a specified file. It should have at least one “Data” class to provide data-related functions such as “decode” and “encode” etc.

“model.py”: the implementation of model classes such as “Head”, “MultiHeadAttention”, “FeedForward”, “Block” and “GPTLanguageMode”.

“trainer.py”: has a “Trainer” class that has a “train” method to train model for a specific number of iterations. The method should print the final loss value.

“main.py”: load data from file, create the model, train the data by specifying the number of iterations, then generate 100 new words. A sample “main.py” file is at the end of this file.
