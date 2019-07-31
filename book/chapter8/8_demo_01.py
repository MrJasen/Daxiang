def print_models(unprinted_designs,completed_models):
    while unprinted_designs:
        temp=unprinted_designs.pop()
        print('正在打印'+temp)
        completed_models.append(temp)

def show_comleted_models(completed_models):
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs=['aaa','bbb','ccc']
completed_models=[]

print_models(unprinted_designs,completed_models)
show_comleted_models(completed_models)