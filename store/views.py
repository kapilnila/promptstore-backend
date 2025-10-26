from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import Prompt

def get_prompts(request):
    prompts = Prompt.objects.all().order_by('-created_at')
    data = [
        {
            "id": p.id,
            "title": p.title,
            "description": p.description,
            "category": p.category,
        }
        for p in prompts
    ]
    return JsonResponse(data, safe=False)
from rest_framework import viewsets
from .models import Prompt
from .serializers import PromptSerializer

class PromptViewSet(viewsets.ModelViewSet):
    queryset = Prompt.objects.all()
    serializer_class = PromptSerializer
# store/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Prompt API!")
