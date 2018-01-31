def make_sandwich(**info):
    profile = { }
    for key,value in info.items():
        profile[key] = value
    return profile

sandwich = make_sandwich(bread='1',sala='sala')
print(sandwich)
