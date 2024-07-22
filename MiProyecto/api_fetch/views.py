from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
import requests

API_URL = 'https://jsonplaceholder.typicode.com/posts'  # Ejemplo de API

def fetch_data_view(request):
    url = 'https://jsonplaceholder.typicode.com/posts'  # Reemplaza con la URL de la API externa
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción para errores HTTP
        data = response.json()  # Asume que la respuesta es JSON
        
        # Formatear los datos obtenidos
        formatted_data = [{'id': item['id'], 'name': item.get('name', 'name')} for item in data]
        print(formatted_data)
        return render(request, 'data_display.html', {'data': formatted_data})
    except requests.exceptions.RequestException as e:
        return HttpResponseBadRequest(f'Error al obtener datos: {str(e)}')


# def get_posts(request):
#     data = fetch_data_view(request)
#     print(data)
#     return JsonResponse(data, safe=False)
