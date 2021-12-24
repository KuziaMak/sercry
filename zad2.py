import json
def write_order_to_json(item,quantity,price,buyer,date):

    with open('orders.json') as f:
        dict_all = json.load(f)

    dict_all["orders"].append({
        "item":item,
        "quantity":quantity,
        "price":price,
        "buyer":buyer,
        "date":date
    })
    with open('orders.json', 'w') as f:
        json.dump(dict_all, f,indent=4)


write_order_to_json("eda","45","23$","Kylerr","20.14")
write_order_to_json("vada","22","66$","sf","20.14")
write_order_to_json("live","88","34$","jjjg","20.14")