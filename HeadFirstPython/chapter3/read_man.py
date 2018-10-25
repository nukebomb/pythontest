import pickle

new_man = []

try:
  with open('man.txt', 'rb') as man_file:
    new_man = pickle.load(man_file)
except IOError as err:
  print('IO error: ' + str(err))
except pickle.PickleError as perr:
  print('PickleError : ' + str(perr))      