import torch
from emissions_calculator.modelDef import model

cat_to_vec = {'Sports & Outdoors': 1, 'Clothing, Shoes & Jewelry': 2, 'Home & Kitchen': 3, 'Baby Products': 4, 'Pet Supplies': 5, 'Arts, Crafts & Sewing': 6, 'Electronics': 7, 'Video Games': 8, 'Patio, Lawn & Garden': 9, 'Tools & Home Improvement': 10, 'Office Products': 11, 'Grocery & Gourmet Food': 12, 'Remote & App Controlled Vehicle Parts': 13, 'Health & Household': 14, 'Industrial & Scientific': 15, 'Beauty & Personal Care': 16, 'Hobbies': 17, 'Remote & App Controlled Vehicles & Parts': 18, 'Automotive': 19, 'Musical Instruments': 20, 'Movies & TV': 21, 'Cell Phones & Accessories': 22, 'Toys & Games': 23, 'Appliances': 24, 'Books': 25, 'Mobility & Daily Living Aids': 26, 'Power & Hand Tools': 27, 'Medical Supplies & Equipment': 28, 'Kitchen & Dining': 29, 'Motorcycle & Powersports': 30, 'CDs & Vinyl': 31, 'Small Appliance Parts & Accessories': 32, 'Office Electronics': 33, 'Instrument Accessories': 34}

def predict(text, text_pipeline):
    vec_to_cat = {v: k for k, v in cat_to_vec.items()}
    with torch.no_grad():
        text = torch.tensor(text_pipeline(text))
        output = model(text, torch.tensor([0]))
        return output.argmax(1).item() + 1