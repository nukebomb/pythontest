
def get_coach_data (fliename):
    try:
        with open(fliename) as f:
            data = f.readline()
        return(data.strip().split(','))
    except IOError as ioerr:
        print('FILE EORRO: ' + ioerr)
        return(None)

james = get_coach_data('james.txt')
julie = get_coach_data('julie.txt')
mikey = get_coach_data('mikey.txt')
sarah = get_coach_data('sarah.txt')        


def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + '.' + secs)

james = sorted(set([sanitize(each_t) for each_t in james]))
julie = sorted(set([sanitize(each_t) for each_t in julie]))
mikey = sorted(set([sanitize(each_t) for each_t in mikey]))
sarah = sorted(set([sanitize(each_t) for each_t in sarah]))

# unique_james = []
# for each_t in james:
#     if each_t not in unique_james:
#         unique_james.append(each_t)

# def get_unique(data):
#     unique_data = []
#     for each_t in data:
#         if each_t not in unique_data:
#             unique_data.append(each_t)
#     return unique_data        

# unique_james = get_unique(james)
# unique_julie = get_unique(julie)
# unique_mikey = get_unique(mikey)
# unique_sarah = get_unique(sarah)

# print(unique_james[0:3])        
# print(unique_julie[0:3])        
# print(unique_mikey[0:3])        
# print(unique_sarah[0:3])        

print(james[0:3])
print(julie[0:3])
print(mikey[0:3])
print(sarah[0:3])
