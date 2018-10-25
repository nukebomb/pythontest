import pickle
man = []
other = []
try:
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('data file is missing')

try:
    with open('man.txt', 'wb') as man_file:
      pickle.dump(man, man_file)
    with open('other.txt', 'wb') as other_file:
      pickle.dump(other, other_file)
except IOError:
    print('file error')
except pickle.PickleError as perr:
  print('pickle error: ' + str(perr))    

