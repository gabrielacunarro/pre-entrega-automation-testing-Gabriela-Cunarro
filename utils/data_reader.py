import csv
import json

def read_users_csv():
    with open("data/users.csv",newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)
    
def read_products_json():
    with open("data/products.json") as file:
<<<<<<< HEAD
        return json.load(file)
=======
        return json.load(file)
    
>>>>>>> e3d064a7da372905a51d3fe2351190578c1b957c
