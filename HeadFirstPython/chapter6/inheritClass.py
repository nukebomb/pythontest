class NameList(list):
    def __init__(self, a_name):
        list.__init__([])
        self.name = a_name


jhon = NameList('jhon paul jhones')


jhon.append('bass palyer')
print(jhon)
jhon.extend(['composer', 'arranger', 'musician'])
print(jhon)

print(jhon.name)

for attr in jhon:
    print(jhon.name + 'is a ' + attr + '.')
