def print_models(unprint_designs,completed_models):
    #模拟打印每个设计，直到没有未打印的设计为止
    #打印每个设计后，都将骑移动到completed_models 中
    while unprint_designs:
        current_design = unprint_designs.pop()

        #模拟根据设计3d打印模型的过程
        print("Printing model" + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    #显示打印好的所有模型
    print("\n The following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprint_designs = ['iphone case','rpbot pendant','dodecahedron']
completed_models = []
print_models(unprint_designs,completed_models)
show_completed_models(completed_models)