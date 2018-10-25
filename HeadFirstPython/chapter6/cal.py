def get_coach_data(fliename):
    file_data = {}
    try:
        with open(fliename) as f:
            data = f.readline()
        templ = data.strip().split(',')
        # file_data['name'] = data.pop(0)
        # file_data['bod'] = data.pop(0)
        # file_data['time'] = sorted([sanitize(each_t) for each_t in data])[0:3]
        # return file_data
        return ({
          'name': templ.pop(0),
          'bod': templ.pop(0),
          'times': sorted([sanitize(each_t) for each_t in templ])[0:3]
        })
    except IOError as ioerr:
        print('FILE EORRO: ' + ioerr)
        return(None)


def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + '.' + secs)

# sarah = get_coach_data('sarah.txt')
# (sarah_name, sarah_dob) = sarah.pop(0), sarah.pop(0)
# print(sarah_name + "'s fastes: " + str(sorted(set([sanitize(t) for t in sarah]))[0:3]))

print(get_coach_data('sarah.txt'))

# sarah_data = {}
# sarah = get_coach_data('sarah.txt')
# (sarah_data['name'], sarah_data['bod'], sarah_data['time']) = sarah.pop(0), sarah.pop(0),sorted([sanitize(each_t) for each_t in sarah]) 
# print(sarah_data)
