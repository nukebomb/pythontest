try:
  data = open('missing.txt')
  print(data.readline(), end='')
except IOError as err:
  print('file roor: ' + str(err))
finally:
  if 'data' in locals():
    data.close()  