from emissions_calculator.vocab import data
from emissions_calculator.vocab import vocab
from emissions_calculator.modelClass import TextClassificationModel
import pandas
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
train_iter = list(data[['Category', 'Product Name']].itertuples(index=False, name=None))
# again might need to rewrite train iter to not be an iterable
num_class = len(set([label for (label, text) in train_iter]))
vocab_size = len(vocab)
print(vocab_size, num_class)
emsize = 64
model = TextClassificationModel(vocab_size, emsize, num_class).to(device)