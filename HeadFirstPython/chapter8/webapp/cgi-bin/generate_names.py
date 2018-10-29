import json
import athletemodel
import yate
print(123)
names = athletemodel.get_names_from_store()

print(yate.start_response('application/json'))
print(json.dumps(names))