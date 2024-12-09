import torch

def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
