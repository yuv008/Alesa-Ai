from django.urls import path
from . import views

urlpatterns = [
    path('interpret/', views.interpret_dream, name='interpret-dream'),
]