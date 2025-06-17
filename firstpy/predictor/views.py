from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .predict import predict_fitness

@csrf_exempt
def check_fitness(request):
    if request.method == "POST":
        data = json.loads(request.body)
        is_fit = predict_fitness(data)
        return JsonResponse({"fit": is_fit})
    return JsonResponse({"error": "Only POST method allowed"}, status=405)
