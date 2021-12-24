import yaml
dict_full = {
    "lisen": [1,2,3],
    "integ": 5,
    "dict":{
        "€":"evro",
        "Њ":"чо-то",
        "Ћ":"стул"
    }
}
with open("file.yaml", "w") as f:
    yaml.dump(dict_full, f, default_flow_style=True, allow_unicode = True)
with open("file.yaml") as f:
    readin = yaml.load(f, Loader=yaml.FullLoader)

print(readin)

if dict_full==readin:
    print("ura")