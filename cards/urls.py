from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import CardListView, CardUpdateView, CardCreateView, CardDeleteView, add_to_deck

app_name = 'cards'
urlpatterns = [
    path('', CardListView.as_view(), name='list'),
    path('new/', login_required(CardCreateView.as_view()), name='create'),
    path('<int:pk>/', login_required(CardUpdateView.as_view()), name='update'),
    path('<int:card_id>/to/<int:deck_id>', login_required(add_to_deck), name='add_to_deck'),
    path('<int:pk>/delete/', login_required(CardDeleteView.as_view()), name='delete'),
]