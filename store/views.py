from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import Prompt

def prompt_list(request):
    data = list(Prompt.objects.values())
    return JsonResponse(data, safe=False)
