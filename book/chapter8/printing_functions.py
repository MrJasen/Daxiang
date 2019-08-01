def print_models(unprinted_designs,completed_models):
    while unprinted_designs:
        temp=unprinted_designs.pop()
        print('正在打印'+temp)
        completed_models.append(temp)