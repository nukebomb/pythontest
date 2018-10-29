import cgi
import cgitb
cgitb.enable()
import yate
import athletemodel

athletes = athletemodel.get_from_store()

form_data = cgi.FieldStorage()
athlete_name = form_data['which_athlete'].value

print(yate.start_response())
print(yate.include_header('coach keyy timing data'))
print(yate.header('Athlete: ' + athlete_name + ',dob: ' + athletes[athlete_name].dob + '.'))
print(yate.para('the top times for this athlete are :'))
print(yate.u_list(athletes[athlete_name].top3))
print(yate.include_footer({'home':'/index.html','selecte anther athlere': 'generate_list.py'}))
