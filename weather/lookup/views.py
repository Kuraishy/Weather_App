from django.shortcuts import render

# Create your views here.

def home(request):
	import json
	import requests

	api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=5&API_KEY=1B384AA4-1968-4F64-A65E-7E4C536F160E")

	try:
		api = json.loads(api_request.content)
		categoryDescription, categoryColor = weatherStatus(api)


	except Exception as e:
		print(e)
		api = e


	return render(request, 'home.html',{'api':api, 'category_description':categoryDescription, 'category_color':categoryColor}) 

def about(request):
	return render(request, 'about.html',{}) 


def weatherStatus(api):
	categoria = api[0]['Category']['Name']
	categoriaColor=''

	if categoria == "Good":
		return f"(0-50) Air quality is considered satisfactory, and air pollution poses litthle or no risk", "good"

	elif categoria == "Moderate":
		return f"(51-100) Air quality is considered aceptable", "moderate"

	elif categoria == "Unhealthy for Sensitive Groups":
		return f"(101-150) Air quality is considered unhealthy for people with some ilnesses", "usg"

	elif categoria == "Unhealthy":
		return "(151-200) Air quality is considered unhealthy", "unhealthy"

	elif categoria == "Very Unhealthy":
		return "(201-300) Air quality is considered unhealthy", "veryunhealthy"

	elif categoria == "Hazardous":
		return "(301-500) Air quality is considered hell ","hazardous"

