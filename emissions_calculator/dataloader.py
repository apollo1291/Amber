from torch.utils.data import DataLoader
from vocab import label_pipeline
from vocab import text_pipeline
from vocab import data
import torch


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def collate_batch(batch):
    label_list, text_list, offsets = [], [], [0]
    for (_label, _text) in batch:
         label_list.append(label_pipeline(_label))
         processed_text = torch.tensor(text_pipeline(_text), dtype=torch.int64)
         text_list.append(processed_text)
         offsets.append(processed_text.size(0))
    label_list = torch.tensor(label_list, dtype=torch.int64)
    offsets = torch.tensor(offsets[:-1]).cumsum(dim=0)
    text_list = torch.cat(text_list)
    return label_list.to(device), text_list.to(device), offsets.to(device)


# train_iter may need to be rewritten so its not an iterable, ie list(data[['Category', 'Product Name']].itertuples(index=False, name=None))
train_iter = list(data[['Category', 'Product Name']].itertuples(index=False, name=None))
dataloader = DataLoader(train_iter, batch_size=8, shuffle=False, collate_fn=collate_batch)