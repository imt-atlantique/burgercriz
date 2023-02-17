from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse

from .models import Card, Tag, Deck

class CardCreateView(CreateView):
    model = Card
    fields = ['text', 'type', 'public', 'tags']

    success_url = '/cards/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        
        return super().form_valid(form)

class CardListView(ListView):
    model = Card
    paginate_by = 21

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        context['public_decks'] = Deck.objects.filter(public=True)
        if self.request.user.is_authenticated:
            context['decks'] = Deck.objects.filter(public=True, user = self.request.user)
        return context

    def get_queryset(self):
        tag = self.request.GET.get('tag')
        deck = self.request.GET.get('deck')
        if tag:
            self.tag = get_object_or_404(Tag, tag__startswith=tag)
            return Card.objects.filter(tags=self.tag).order_by('-modified_date')
        if deck:
            self.deck = get_object_or_404(Deck, name__startswith=deck)
            return self.deck.cards.filter(public=True).order_by('-modified_date')
        else:
            return Card.objects.filter(public=True).order_by('-modified_date')

class CardUpdateView(UpdateView):
    model = Card
    fields = ['text', 'type', 'public', 'tags']
    success_url = '/cards/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['decks'] = Deck.objects.filter(user=self.request.user)
        return context

    def dispatch(self, request, *args, **kwargs):
        card = get_object_or_404(Card, pk=self.kwargs['pk'])
        if request.user != card.user:
            return HttpResponseForbidden("Dis donc, c'est interdit ça d'éditer la carte des petits copains !")
        return super().dispatch(request, *args, **kwargs)

class CardDeleteView(DeleteView):
    model = Card
    success_url = '/cards/'

    def dispatch(self, request, *args, **kwargs):
        card = get_object_or_404(Card, pk=self.kwargs['pk'])
        if request.user != card.user:
            return HttpResponseForbidden("Dis donc, c'est interdit ça de supprimer la carte des petits copains !")
        return super().dispatch(request, *args, **kwargs)

class DeckCreateView(CreateView):
    model = Deck
    fields = ['name', 'public']

    success_url = '/cards/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        
        return super().form_valid(form)

def add_to_deck(request, card_id, deck_id):
    card = get_object_or_404(Card, pk=card_id)
    if request.user.is_authenticated:
        deck = get_object_or_404(Deck, pk=deck_id, user=request.user)
    if card in deck.cards.all():
        deck.cards.remove(card)
    else:
        deck.cards.add(card)

    return HttpResponseRedirect(reverse('cards:list'))