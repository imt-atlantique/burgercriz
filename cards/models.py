from django.db import models
from django.contrib.auth.models import User

from markdownfield.models import MarkdownField, RenderedMarkdownField
from markdownfield.validators import VALIDATOR_NULL


class Tag(models.Model):
    tag = models.SlugField(blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    created_date = models.DateTimeField('Date de création', auto_now_add=True)

    def __str__(self):
        return self.tag


class Card(models.Model):
    text = MarkdownField('Texte de la carte', rendered_field='text_rendered', validator=VALIDATOR_NULL, default="Tapez le texte de votre carte (en utilisant **Markdown**)")
    text_rendered = RenderedMarkdownField('Texte de la carte en HTML')
    TYPE_CHOICES = (
        (0, "Toss"),
        (1, "Nuggets"),
        (2, "Sel ou poivre"),
        (3, "Menu (cordon bleu)"),
        (4, "Menu (cordon rouge)"),
        (5, "L'addition"),
        (6, "Burger de la mort"),

    )

    type = models.PositiveSmallIntegerField(
        'Type de carte', choices=TYPE_CHOICES, default=1)
    public = models.BooleanField('Carte publique ?', default=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)

    modified_date = models.DateTimeField('Date de modification', auto_now=True)
    created_date = models.DateTimeField('Date de création', auto_now_add=True)

    def __str__(self):
        return "Carte " + str(self.TYPE_CHOICES[self.type][1]).lower() + ' n°' + str(self.id)

    class Meta:
        verbose_name = "Carte"
        verbose_name_plural = "Cartes"


class Deck(models.Model):
    name = models.CharField('Paquet de cartes', max_length=128)
    cards = models.ManyToManyField(Card, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    public = models.BooleanField('Paquet public ?', default=True)

    created_date = models.DateTimeField('Date de création', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Paquet de cartes"
        verbose_name_plural = "Paquets de cartes"
