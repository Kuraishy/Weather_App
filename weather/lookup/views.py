from django.shortcuts import render

# Create your views here.

def home(request):
	import json
	import requests

	api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=5&API_KEY=1B384AA4-1968-4F64-A65E-7E4C536F160E")

	try:
		api = json.loads(api_request.content)

	except Exception as e:
		print(e)
		api = e

	return render(request, 'home.html',{'api':api}) 

def about(request):
	return render(request, 'about.html',{}) 