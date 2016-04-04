import requests
import pprint

response = requests.get('http://localhost:8000/api/')
print response.status_code

api = response.json()
pprint.pprint(api)

response = requests.get(api['sprints'])
response.status_code


import datetime
today = datetime.date.today()
two_weeks = datetime.timedelta(days=14)
data = {'name': 'Current Sprint', 'end': today + two_weeks}
response = requests.post(api['sprints'], data=data, auth=('demo','demo'))
response.status_code

sprint = response.json()
pprint.pprint(sprint)

data = {'name': 'Something Task', 'sprint': sprint['id']}
response = requests.post(api['tasks'], data=data, auth=('demo','demo'))

task['assigned'] = 'demo'
task['status'] = 2
task['started'] = today
response = requests.put(task['links']['self'],
	data=task,auth=('demo','demo'))

response.status_code
task = response.json()

pprint.pprint(task)