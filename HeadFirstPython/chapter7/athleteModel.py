import pickle
from athleteList import AthleteList


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

def put_to_store(flies_list):        
    all_athletes = {}
    for each_file in flies_list:
      ath = get_coach_data(each_file)
      all_athletes[ath.name] = ath
    try:
      with open('athletes.pickle', 'wb') as athf:
        pickle.dump(all_athletes, athf)
    except IOError as ioerr:
      print('files error(put_adn_sotre): ' + str(ioerr))      
    return(all_athletes)

def get_from_store():
  all_athletes = {}    
  try:
    with open('athletes.pickle', 'rb') as athf:
      all_athletes = pickle.load(athf)
  except IOError as ioerr:
    print('files error(get_from_sotre): ' + str(ioerr))
  return (all_athletes)        

the_files = ['sarah.txt', 'james.txt','mikey.txt','julie.txt']
data = put_to_store(the_files)
print(data)
for each_athlete in data:
  print(data[each_athlete].name + ' ' + data[each_athlete].dob)

data_copy = get_from_store()
for each_athlete in data_copy:
  print(data_copy[each_athlete].name + ' ' + data_copy[each_athlete].dob)