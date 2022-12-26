from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import CardListView, CardUpdateView

app_name = 'cards'
urlpatterns = [
    path('', CardListView.as_view(), name='list'),
    path('<int:pk>/', login_required(CardUpdateView.as_view()), name='update'),
]