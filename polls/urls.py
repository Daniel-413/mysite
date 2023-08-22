from django.urls import path
from .views import IndexView, QuestionView

urlpatterns = [
    path('', IndexView.as_view(),name='index'),
    path('pergunta/<int:pk>', QuestionView.as_view(),name='question'),
]