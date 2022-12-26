from django.views.generic import ListView, UpdateView
from .models import Card

class CardListView(ListView):
    model = Card

class CardUpdateView(UpdateView):
    model = Card
    fields = ['text', 'type', 'public', 'tags']