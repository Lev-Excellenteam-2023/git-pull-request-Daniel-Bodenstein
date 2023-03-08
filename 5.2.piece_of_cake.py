def get_recipe_price_5_2(d, optionals = [] , **kargs):
    #sum = 0
    #for key in d.keys():
    #    if key not in optionals:
    #        sum += d[key]*kargs[key]/100
    sum = sum(map(lambda key: d[key]*kargs[key]/100, filter(lambda key: key not in optionals, d.keys())))
    print(sum)