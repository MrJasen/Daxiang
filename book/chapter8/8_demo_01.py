import printing_functions


def show_comleted_models(completed_models):
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs=['aaa','bbb','ccc']
completed_models=[]

print_models(unprinted_designs,completed_models)
show_comleted_models(completed_models)