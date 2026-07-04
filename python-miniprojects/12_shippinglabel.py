print("--------SHIPPING LABEL--------")
def shipping_lable(*args,**kwargs):
    for arg in args:
        print(arg,end=" ")
    print()
    if "apt" in kwargs:
        print(f"{kwargs.get('street') }{ kwargs.get('apt')}")
    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('zip')}")
    print(f"{kwargs.get('city')}")
shipping_lable("Mr","John","Doe","III",
               street="107 landlow st.",
               apt=" 127",
               city="New York",
               zip="97868")