import torch
from model import BigramLanguageModel
from data import load_data, split_data, get_batch

# Hyperparameters
batch_size = 16
block_size = 8
max_iters = 100
eval_interval = 500
learning_rate = 0.01
device = 'cuda' if torch.cuda.is_available() else 'cpu'
eval_iters = 50
n_embd = 32
n_head = 4
n_layer = 3
dropout = 0.2
