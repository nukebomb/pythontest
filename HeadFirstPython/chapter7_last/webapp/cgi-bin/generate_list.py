import athletemodel
import yate
import glob


data_files = glob.glob('data/*.txt')
athletes = athletemodel.put_to_store(data_files)

print(yate.start_response())
print(yate.include_header("list of athletes"))
print(yate.start_form('generate_timing_data.py'))
print(yate.para('selecte an athlete: '))
for each_athlete in athletes:
  print(yate.radio_button('which_athlete',athletes[each_athlete].name))  
print(yate.end_form())
print(yate.include_footer({'home':'/index.html'}))