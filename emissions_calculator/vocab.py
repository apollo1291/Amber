from torchtext.data.utils import get_tokenizer
from torchtext.vocab import build_vocab_from_iterator
import pandas as pd
import numpy as np

# read the csv data out
data = pd.read_csv("./Data/ProductData.csv")

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1500)

cat_to_vec = {'Sports & Outdoors': 1, 'Clothing, Shoes & Jewelry': 2, 'Home & Kitchen': 3, 'Baby Products': 4, 'Pet Supplies': 5, 'Arts, Crafts & Sewing': 6, 'Electronics': 7, 'Video Games': 8, 'Patio, Lawn & Garden': 9, 'Tools & Home Improvement': 10, 'Office Products': 11, 'Grocery & Gourmet Food': 12, 'Remote & App Controlled Vehicle Parts': 13, 'Health & Household': 14, 'Industrial & Scientific': 15, 'Beauty & Personal Care': 16, 'Hobbies': 17, 'Remote & App Controlled Vehicles & Parts': 18, 'Automotive': 19, 'Musical Instruments': 20, 'Movies & TV': 21, 'Cell Phones & Accessories': 22, 'Toys & Games': 23, 'Appliances': 24, 'Books': 25, 'Mobility & Daily Living Aids': 26, 'Power & Hand Tools': 27, 'Medical Supplies & Equipment': 28, 'Kitchen & Dining': 29, 'Motorcycle & Powersports': 30, 'CDs & Vinyl': 31, 'Small Appliance Parts & Accessories': 32, 'Office Electronics': 33, 'Instrument Accessories': 34}

data.replace(to_replace=cat_to_vec, inplace=True)

#export as function?
# create an array of product name values
make_vocab = list(data[['Category', 'Product Name']].itertuples(index=False, name=None))
# make the array an iterable
train_iter = iter(make_vocab)

tokenizer = get_tokenizer('basic_english')

def yield_tokens(data_iter):
    for _, text in data_iter:
        yield tokenizer(text)

vocab = build_vocab_from_iterator(yield_tokens(train_iter), specials=["<unk>"])
vocab.set_default_index(vocab["<unk>"])

#export
text_pipeline = lambda x: vocab(tokenizer(x))
#export
label_pipeline = lambda x: int(x) - 1