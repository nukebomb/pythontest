import os


def read_file(data):
    for each_line in data:
      try:
        (role, line_spoken) = each_line.split(':', 1)
        print(role, end='')
        print(' said: ', end='')
        print(line_spoken, end='')
      except ValueError:
        print(each_line)
    data.close()


try:
    data_real = open('sketch.txt')
    read_file(data_real)
except IOError:
    print('file is missing')
