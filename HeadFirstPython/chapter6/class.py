class Athlete:
    def __init__(self, a_name, a_dob=None, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times

    def top3(self):
        templ = self.times
        return sorted([sanitize(each_t) for each_t in templ])[0:3]

    def add_time(self, time_value):
      self.times.append(time_value)
    def add_times(self, time_list):
      self.times.extend(time_list)  

def get_coach_data(fliename):
    file_data = {}
    try:
        with open(fliename) as f:
            data = f.readline()
        templ = data.strip().split(',')
        return Athlete(templ.pop(0), templ.pop(0), templ)
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


vera = Athlete('vera vi', '2018-10-27', ['2.22', '2.23'])
print(vera.top3())
vera.add_time('1.22')
print(vera.top3())
vera.add_times(['0.65','2.01'])
print(vera.top3())

