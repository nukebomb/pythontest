class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    def top3(self):
        return sorted([sanitize(each_t) for each_t in self])[0:3]


def get_coach_data(fliename):
    file_data = {}
    try:
        with open(fliename) as f:
            data = f.readline()
        templ = data.strip().split(',')
        return AthleteList(templ.pop(0), templ.pop(0), templ)
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

def show_list(list_data):
    print(list_data.name + "'s fatest times are: " + str(list_data.top3()))

# james = get_coach_data('james.txt')
# julie = get_coach_data('julie.txt')
# mikey = get_coach_data('mikey.txt')
# sarah = get_coach_data('sarah.txt')

# show_list(james)
# show_list(julie)
# show_list(mikey)
# show_list(sarah)
