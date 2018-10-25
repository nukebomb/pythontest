def print_list(list_all, level=0):
    for item in list_all:
        if isinstance(item, list):
            print_list(item, level+1)
        else:
            for tab_stop in range(level):
                print('\t', end='')
            print(item)

print_list(['x','y',['aa','bb',['xx','yyy']]])            
            
