
# store/urls.py
from django.urls import path, include
from .views import PromptViewSet, home
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'prompts', PromptViewSet)

urlpatterns = [
    path('', home, name='home'),         # root URL
    path('api/', include(router.urls)),  # DRF endpoints
]
